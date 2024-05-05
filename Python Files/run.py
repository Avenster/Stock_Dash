import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, start_date, end_date):
    stock = yf.download(symbol, start=start_date, end=end_date)
    return stock

def save_to_csv(df, filename):
    df.to_csv(filename)

if __name__ == "__main__":
    symbol = "^NSEI"
    start_date = "2019-04-22"
    end_date = "2024-05-03"

    stock_data = fetch_stock_data(symbol, start_date, end_date)
    stock_data = stock_data[['Open', 'High', 'Low', 'Close']]  # Select required columns
    stock_data.columns = map(str.lower, stock_data.columns)  # Convert column names to lowercase
    stock_data.reset_index(inplace=True)  # Reset index to make 'Date' a column
    stock_data.rename(columns={'Date': 'time'}, inplace=True)  # Rename 'Date' to 'time'
    stock_data.set_index('time', inplace=True)  # Set 'time' as index
    
    save_to_csv(stock_data, "Nifty50_data.csv")

# def fetch_stock_data(symbol, start_date, end_date):
#     stock = yf.download(symbol, start=start_date, end=end_date)
#     return stock[['Close']]  # Returning a DataFrame with only the 'Close' column

# def save_to_csv(df, filename):
#     df.to_csv(filename)

# if __name__ == "__main__":
#     symbol = "^NSEI"
#     start_date = "2019-04-22"
#     end_date = "2024-05-03"

#     stock_data = fetch_stock_data(symbol, start_date, end_date)
#     stock_data.reset_index(inplace=True)  # Reset index to make 'Date' a column
#     stock_data.rename(columns={'Date': 'time', 'Close': 'value'}, inplace=True)  # Rename 'Date' to 'time' and 'Close' to 'close'
#     stock_data.set_index('time', inplace=True)  # Set 'time' as index
    
#     save_to_csv(stock_data, "Nifty50_Close_data.csv")