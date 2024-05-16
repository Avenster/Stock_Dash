# import yfinance as yf
# import pandas as pd

# ticker_symbols_with_names = {
#     '000001.SS': 'SSE Composite Index (China)',
#     '^AEX': 'AEX (Netherlands)',
#     '^ATX': 'ATX (Austria)',
#     '^AXJO': 'S&P/ASX 200 (Australia)',
#     '^BFX': 'BEL 20 (Belgium)',
#     '^BSESN': 'BSE Sensex (India)',
#     '^BVSP': 'Bovespa Index (Brazil)',
#     '^FCHI': 'CAC 40 (France)',
#     '^GDAXI': 'DAX (Germany)',
#     '^GSPC': 'S&P 500 (United States)',
#     '^GSPTSE': 'S&P/TSX Composite Index (Canada)',
#     '^HSI': 'Hang Seng Index (Hong Kong)',
#     '^IBEX': 'IBEX 35 (Spain)',
#     '^ISEQ': 'ISEQ 20 (Ireland)',
#     '^IXIC': 'NASDAQ Composite (United States)',
#     '^JKSE': 'Jakarta Composite Index (Indonesia)',
#     '^KS11': 'KOSPI (South Korea)',
#     '^MERV': 'MERVAL (Argentina)',
#     '^MXX': 'IPC (Mexico)',
#     '^N225': 'Nikkei 225 (Japan)',
#     '^NSEBANK': 'NSE Bank Index (India)',
#     '^NSEI': 'Nifty 50 (India)',
#     '^NYA': 'NYSE Composite (United States)',
#     '^SET.BK': 'SET Index (Thailand)',
#     '^SSMI': 'SMI (Switzerland)',
#     '^STI': 'Straits Times Index (Singapore)',
#     '^TWII': 'Taiwan Weighted Index (Taiwan)',

# }

# index_data = {}
# for ticker_symbol, stock_name in ticker_symbols_with_names.items():
#     data = yf.download(ticker_symbol, start='2024-05-09', end='2024-05-10')
#     if len(data) > 0:
#         index_data[ticker_symbol] = {'StockName': stock_name, 'AdjClose': data['Adj Close']}
#     else:
#         print(f"No data available for {ticker_symbol}")

# combined_data = pd.DataFrame(index=index_data[next(iter(index_data))]['AdjClose'].index)
# for ticker_symbol, data in index_data.items():
#     stock_name = data['StockName']
#     combined_data[f"{ticker_symbol} {stock_name}"] = data['AdjClose']

# combined_data['^SSMI SMI (Switzerland)'] = 11753.70


# combined_data.index.name = 'Date'
# combined_data = combined_data.reindex(sorted(combined_data.columns), axis=1)

# csv_file_path = 'recent.csv'
# combined_data.to_csv(csv_file_path)

# print("Combined data saved to", csv_file_path)

import json

# Load existing data from predicted_price.json
try:
    with open('predicted_price.json', 'r') as f:
        existing_data = json.load(f)
except FileNotFoundError:
    existing_data = {}

# Load data from data.json
with open('data.json', 'r') as f:
    data = json.load(f)

# Get the correlation matrices
correlation_matrices = data['correlation']

# Calculate the length of the correlation matrices list
num_matrices = len(correlation_matrices)

# Update the existing data with the new key-value pair
existing_data['num_matrices'] = num_matrices

# Save the updated data in predicted_price.json
with open('predicted_price.json', 'w') as f:
    json.dump(existing_data, f, indent=4)