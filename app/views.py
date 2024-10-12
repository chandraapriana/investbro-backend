from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
import yfinance as yf
import json
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Constants
VALID_PERIODS = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
CACHE_TIMEOUT = 60 * 5  # 5 minutes

# --- Utility Functions ---

# Function to validate stock input
def validate_input(item):
    name = item.get('name')
    start_date = item.get('start_date')
    end_date = item.get('end_date')
    period = item.get('period')

    if not name or not isinstance(name, str):
        return False, 'Stock name must be a valid non-empty string'
    
    if period and (start_date or end_date):
        return False, 'Provide either period or both start_date and end_date, not both'
    
    if not period and (not start_date or not end_date):
        return False, 'Provide either period or both start_date and end_date'
    
    if period and period not in VALID_PERIODS:
        return False, f'Invalid period. Valid periods: {", ".join(VALID_PERIODS)}'

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

# Function to get a unique cache key based on input
def get_cache_key(name, start_date=None, end_date=None, period=None):
    if period:
        return f'{name}_{period}'
    else:
        return f'{name}_{start_date}_{end_date}'

# Function to fetch stock data and check cache
def fetch_stock_data(name, start_date=None, end_date=None, period=None):
    cache_key = get_cache_key(name, start_date, end_date, period)
    cached_data = cache.get(cache_key)

    # Check if cached data exists
    if cached_data is not None:
        return cached_data

    stock = yf.Ticker(name)
    hist = stock.history(period=period) if period else stock.history(start=start_date, end=end_date)

    if not hist.empty:
        cache.set(cache_key, hist, CACHE_TIMEOUT)
    
    return hist

# Convert yfinance history data to dictionary
def convert_history_to_dict(hist):
    return {date.strftime('%Y-%m-%d'): value for date, value in hist['Close'].items()}

# Generalized function to process asset data
def process_asset(item):
    valid, error_message = validate_input(item)
    if not valid:
        return None, {'error': error_message}, 400

    name = item['name']
    original_name = item['name'].replace('.JK', '').replace("-USD", "").replace("GC=F", "GOLD").replace("=X", "")
    start_date = item.get('start_date')
    end_date = item.get('end_date')
    period = item.get('period')

    hist = fetch_stock_data(name, start_date, end_date, period)
    if hist.empty:
        return None, {'error': f'No data found for {item["name"]}'}, 404

    return original_name, convert_history_to_dict(hist), 200

# Function to handle JSON request data
def handle_post_request(request):
    try:
        data = json.loads(request.body)
        if not isinstance(data, list) or len(data) == 0:
            return None, JsonResponse({'error': 'Payload must be a non-empty list'}, status=400)
        return data, None
    except json.JSONDecodeError:
        return None, JsonResponse({'error': 'Invalid JSON payload'}, status=400)

# Process stock data in parallel
def process_data_in_parallel(data):
    stock_data = {}
    errors = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_asset, item) for item in data]
        for future in as_completed(futures):
            result = future.result()
            name, data_or_error, status = result
            if status != 200:
                errors.append(data_or_error)
            else:
                stock_data[name] = data_or_error
    return stock_data, errors

# Function to call post_stock_data with modified names
def post_stock_data_with_updated_names(data):
    request = type('Request', (object,), {})()  # Create a mock request object
    request.method = 'POST'
    request.body = json.dumps(data).encode('utf-8')  # Convert data to JSON string, then to bytes
    request.META = {'CONTENT_TYPE': 'application/json'}  # Set content type

    # Call the existing post_stock_data function with the modified request
    return post_stock_data(request)

# --- View Functions ---

@csrf_exempt
def post_stock_data(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    data, error_response = handle_post_request(request)
    if error_response:
        return error_response

    stock_data, errors = process_data_in_parallel(data)

    if errors:
        return JsonResponse(errors[0], status=errors[0].get('status', 400))

    return JsonResponse(stock_data, status=200)

# Generalized function to append suffix or set ticker directly
def set_ticker_directly_or_append_suffix(request, ticker=None, suffix=None):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    data, error_response = handle_post_request(request)
    if error_response:
        return error_response

    for item in data:
        if isinstance(item, dict):
            if ticker:
                item['name'] = ticker  # Set ticker directly (for gold or specific assets)
            elif suffix:
                item['name'] = f"{item['name']}{suffix}"  # Append suffix (for stock/forex)

    return post_stock_data_with_updated_names(data)

@csrf_exempt
def post_stock_id_data(request):
    return set_ticker_directly_or_append_suffix(request, suffix='.JK')

@csrf_exempt
def post_crypto_data(request):
    return set_ticker_directly_or_append_suffix(request, suffix='-USD')

@csrf_exempt
def post_gold_data(request):
    return set_ticker_directly_or_append_suffix(request, ticker='GC=F')

@csrf_exempt
def post_forex_data(request, currency1, currency2):
    ticker = f"{currency1}{currency2}=X"
    return set_ticker_directly_or_append_suffix(request, ticker=ticker)
