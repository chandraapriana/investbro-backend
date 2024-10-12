from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache  # Import cache
import yfinance as yf
import json
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

VALID_PERIODS = [
    "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"
]

CACHE_TIMEOUT = 60 * 5  # Waktu cache selama 5 menit (300 detik)

# Fungsi validasi input
def validate_input(item):
    name = item.get('name')
    start_date = item.get('start_date')
    end_date = item.get('end_date')
    period = item.get('period')

    if not name or not isinstance(name, str):
        return False, 'Stock name must be a valid non-empty string'
    
    if period and (start_date or end_date):
        return False, 'You must provide either period or both start_date and end_date, but not both'
    
    if not period and (not start_date or not end_date):
        return False, 'You must provide either period or both start_date and end_date'
    
    if period and period not in VALID_PERIODS:
        return False, f'Invalid period. Valid periods are: {", ".join(VALID_PERIODS)}'
    
    if start_date and end_date:
        try:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

            if start_date > end_date:
                return False, 'start_date cannot be later than end_date'
            
            if end_date > datetime.date.today():
                return False, 'end_date cannot be in the future'
        except ValueError:
            return False, 'Invalid date format. Use YYYY-MM-DD'

    return True, None

# Fungsi untuk mendapatkan cache key unik berdasarkan input
def get_cache_key(name, start_date=None, end_date=None, period=None):
    if period:
        return f'{name}_{period}'
    else:
        return f'{name}_{start_date}_{end_date}'

# Fungsi untuk mengembalikan data saham, dengan memeriksa cache terlebih dahulu
def fetch_stock_data(name, start_date=None, end_date=None, period=None):
    cache_key = get_cache_key(name, start_date, end_date, period)
    cached_data = cache.get(cache_key)  # Cek apakah data ada di cache
    
    if cached_data is not None:
        return cached_data  # Kembalikan data dari cache jika ditemukan

    stock = yf.Ticker(name)
    if period:
        hist = stock.history(period=period)
    else:
        hist = stock.history(start=start_date, end=end_date)

    if not hist.empty:  # Cek jika DataFrame tidak kosong
        cache.set(cache_key, hist, CACHE_TIMEOUT)  # Simpan ke cache jika ada data
    return hist

# Fungsi untuk mengonversi hasil yfinance
def convert_history_to_dict(hist):
    return {date.strftime('%Y-%m-%d'): value for date, value in hist['Close'].items()}

# Fungsi yang dijalankan paralel untuk setiap saham
def process_stock(item):
    valid, error_message = validate_input(item)
    if not valid:
        return None, {'error': error_message}, 400

    name = item['name']
    start_date = item.get('start_date')
    end_date = item.get('end_date')
    period = item.get('period')

    # Ambil data saham dengan caching
    hist = fetch_stock_data(name, start_date, end_date, period)

    if hist.empty:
        return None, {'error': f'No data found for {name} in the given range or period'}, 404

    # Konversi hasil ke dictionary
    return name, convert_history_to_dict(hist), 200

@csrf_exempt
def post_stock_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            if not isinstance(data, list) or len(data) == 0:
                return JsonResponse({'error': 'Payload must be a non-empty list'}, status=400)

            stock_data = {}
            errors = []

            # Menggunakan ThreadPoolExecutor untuk memproses beberapa saham secara paralel
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(process_stock, item) for item in data]

                for future in as_completed(futures):
                    result = future.result()
                    name, data_or_error, status = result

                    if status != 200:
                        errors.append(data_or_error)
                    else:
                        stock_data[name] = data_or_error

            # Jika ada error, kembalikan error pertama yang ditemukan
            if errors:
                return JsonResponse(errors[0], status=errors[0]['status'])

            return JsonResponse(stock_data, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
