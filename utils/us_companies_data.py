from decouple import config
us_companies_data = [
  {
    "ticker": "AAPL",
    "name": "Apple",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/AAPL.png"
  },
  {
    "ticker": "NVDA",
    "name": "NVIDIA",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/NVDA.png"
  },
  {
    "ticker": "MSFT",
    "name": "Microsoft",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/MSFT.png"
  },
  {
    "ticker": "GOOG",
    "name": "Alphabet (Google)",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/GOOG.png"
  },
  {
    "ticker": "AMZN",
    "name": "Amazon",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/AMZN.png"
  },
  {
    "ticker": "META",
    "name": "Meta Platforms (Facebook)",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/META.png"
  },
  {
    "ticker": "BRK-B",
    "name": "Berkshire Hathaway",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/BRK-B.png"
  },
  {
    "ticker": "AVGO",
    "name": "Broadcom",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/AVGO.png"
  },
  {
    "ticker": "LLY",
    "name": "Eli Lilly",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/LLY.png"
  },
  {
    "ticker": "TSLA",
    "name": "Tesla",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/TSLA.png"
  },
  {
    "ticker": "WMT",
    "name": "Walmart",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/WMT.png"
  },
  {
    "ticker": "JPM",
    "name": "JPMorgan Chase",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/JPM.png"
  },
  {
    "ticker": "UNH",
    "name": "UnitedHealth",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/UNH.png"
  },
  {
    "ticker": "XOM",
    "name": "Exxon Mobil",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/XOM.png"
  },
  {
    "ticker": "V",
    "name": "Visa",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/V.png"
  },
  {
    "ticker": "ORCL",
    "name": "Oracle",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/ORCL.png"
  },
  {
    "ticker": "MA",
    "name": "Mastercard",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/MA.png"
  },
  {
    "ticker": "HD",
    "name": "Home Depot",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/HD.png"
  },
  {
    "ticker": "PG",
    "name": "Procter & Gamble",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/PG.png"
  },
  {
    "ticker": "COST",
    "name": "Costco",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/COST.png"
  },
  {
    "ticker": "JNJ",
    "name": "Johnson & Johnson",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/JNJ.png"
  },
  {
    "ticker": "ABBV",
    "name": "AbbVie",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/ABBV.png"
  },
  {
    "ticker": "BAC",
    "name": "Bank of America",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/BAC.png"
  },
  {
    "ticker": "NFLX",
    "name": "Netflix",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/NFLX.png"
  },
  {
    "ticker": "KO",
    "name": "Coca-Cola",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/KO.png"
  },
  {
    "ticker": "MRK",
    "name": "Merck",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/MRK.png"
  },
  {
    "ticker": "CRM",
    "name": "Salesforce",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/CRM.png"
  },
  {
    "ticker": "CVX",
    "name": "Chevron",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/CVX.png"
  },
  {
    "ticker": "AMD",
    "name": "AMD",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/AMD.png"
  },
  {
    "ticker": "TMUS",
    "name": "T-Mobile US",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/TMUS.png"
  },
  {
    "ticker": "PEP",
    "name": "Pepsico",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/PEP.png"
  },
  {
    "ticker": "TMO",
    "name": "Thermo Fisher Scientific",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/TMO.png"
  },
  {
    "ticker": "MCD",
    "name": "McDonald",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/MCD.png"
  },
  {
    "ticker": "ADBE",
    "name": "Adobe",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/ADBE.png"
  },
  {
    "ticker": "CSCO",
    "name": "Cisco",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/CSCO.png"
  },
  {
    "ticker": "IBM",
    "name": "IBM",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/IBM.png"
  },
  {
    "ticker": "WFC",
    "name": "Wells Fargo",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/WFC.png"
  },
  {
    "ticker": "GE",
    "name": "General Electric",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/GE.png"
  },
  {
    "ticker": "ABT",
    "name": "Abbott Laboratories",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/ABT.png"
  },
  {
    "ticker": "AXP",
    "name": "American Express",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/AXP.png"
  },
  {
    "ticker": "DHR",
    "name": "Danaher",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/DHR.png"
  },
  {
    "ticker": "CAT",
    "name": "Caterpillar",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/CAT.png"
  },
  {
    "ticker": "NOW",
    "name": "ServiceNow",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/NOW.png"
  },
  {
    "ticker": "QCOM",
    "name": "QUALCOMM",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/QCOM.png"
  },
  {
    "ticker": "TXN",
    "name": "Texas Instruments",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/TXN.png"
  },
  {
    "ticker": "PM",
    "name": "Philip Morris",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/PM.png"
  },
  {
    "ticker": "UBER",
    "name": "Uber",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/UBER.png"
  },
  {
    "ticker": "VZ",
    "name": "Verizon",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/VZ.png"
  },
  {
    "ticker": "MS",
    "name": "Morgan Stanley",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/MS.png"
  },
  {
    "ticker": "AMGN",
    "name": "Amgen",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/AMGN.png"
  },
  {
    "ticker": "INTU",
    "name": "Intuit",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/INTU.png"
  },
  {
    "ticker": "ISRG",
    "name": "Intuitive Surgical",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/ISRG.png"
  },
  {
    "ticker": "DIS",
    "name": "Walt Disney",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/DIS.png"
  },
  {
    "ticker": "AMAT",
    "name": "Applied Materials",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/AMAT.png"
  },
  {
    "ticker": "NEE",
    "name": "Nextera Energy",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/NEE.png"
  },
  {
    "ticker": "PFE",
    "name": "Pfizer",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/PFE.png"
  },
  {
    "ticker": "RTX",
    "name": "Raytheon Technologies",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/RTX.png"
  },
  {
    "ticker": "SPGI",
    "name": "S&P Global",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/SPGI.png"
  },
  {
    "ticker": "GS",
    "name": "Goldman Sachs",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/GS.png"
  },
  {
    "ticker": "CMCSA",
    "name": "Comcast",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/CMCSA.png"
  },
  {
    "ticker": "LOW",
    "name": "Lowe's Companies",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/LOW.png"
  },
  {
    "ticker": "T",
    "name": "AT&T",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/T.png"
  },
  {
    "ticker": "PGR",
    "name": "Progressive",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/PGR.png"
  },
  {
    "ticker": "UNP",
    "name": "Union Pacific Corporation",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/UNP.png"
  },
  {
    "ticker": "BLK",
    "name": "BlackRock",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/BLK.png"
  },
  {
    "ticker": "LMT",
    "name": "Lockheed Martin",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/LMT.png"
  },
  {
    "ticker": "BKNG",
    "name": "Booking Holdings (Booking.com)",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/BKNG.png"
  },
  {
    "ticker": "HON",
    "name": "Honeywell",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/HON.png"
  },
  {
    "ticker": "SYK",
    "name": "Stryker Corporation",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/SYK.png"
  },
  {
    "ticker": "ANET",
    "name": "Arista Networks",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/ANET.png"
  },
  {
    "ticker": "COP",
    "name": "ConocoPhillips",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/COP.png"
  },
  {
    "ticker": "TJX",
    "name": "TJX Companies",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/TJX.png"
  },
  {
    "ticker": "BSX",
    "name": "Boston Scientific",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/BSX.png"
  },
  {
    "ticker": "C",
    "name": "Citigroup",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/C.png"
  },
  {
    "ticker": "KKR",
    "name": "KKR & Co.",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/KKR.png"
  },
  {
    "ticker": "VRTX",
    "name": "Vertex Pharmaceuticals",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/VRTX.png"
  },
  {
    "ticker": "SCHW",
    "name": "Charles Schwab",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/SCHW.png"
  },
  {
    "ticker": "NKE",
    "name": "Nike",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/NKE.png"
  },
  {
    "ticker": "PANW",
    "name": "Palo Alto Networks",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/PANW.png"
  },
  {
    "ticker": "MU",
    "name": "Micron Technology",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/MU.png"
  },
  {
    "ticker": "ADP",
    "name": "Automatic Data Processing",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/ADP.png"
  },
  {
    "ticker": "ELV",
    "name": "Elevance Health",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/ELV.png"
  },
  {
    "ticker": "ADI",
    "name": "Analog Devices",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/ADI.png"
  },
  {
    "ticker": "UPS",
    "name": "United Parcel Service",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/UPS.png"
  },
  {
    "ticker": "DE",
    "name": "Deere & Company",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/DE.png"
  },
  {
    "ticker": "REGN",
    "name": "Regeneron Pharmaceuticals",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/REGN.png"
  },
  {
    "ticker": "PLD",
    "name": "Prologis",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/PLD.png"
  },
  {
    "ticker": "MMC",
    "name": "Marsh & McLennan Companies",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/MMC.png"
  },
  {
    "ticker": "BX",
    "name": "Blackstone Group",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/BX.png"
  },
  {
    "ticker": "FI",
    "name": "Fiserv",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/FI.png"
  },
  {
    "ticker": "SBUX",
    "name": "Starbucks",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/SBUX.png"
  },
  {
    "ticker": "KLAC",
    "name": "KLA",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/KLAC.png"
  },
  {
    "ticker": "LRCX",
    "name": "Lam Research",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/LRCX.png"
  },
  {
    "ticker": "BMY",
    "name": "Bristol-Myers Squibb",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/BMY.png"
  },
  {
    "ticker": "GILD",
    "name": "Gilead Sciences",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/GILD.png"
  },
  {
    "ticker": "AMT",
    "name": "American Tower",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/AMT.png"
  },
  {
    "ticker": "HCA",
    "name": "HCA Healthcare",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/HCA.png"
  },
  {
    "ticker": "INTC",
    "name": "Intel",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/INTC.png"
  },
  {
    "ticker": "CI",
    "name": "Cigna",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/CI.png"
  },
  {
    "ticker": "PLTR",
    "name": "Palantir",
    "logo": config('BASE_URL')+"/static/images/us_company_logos/PLTR.png"
  }
]
