from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

tickers = ['INDEXNSE', 'INDEXSP', 'INDEXNASDAQ']
exchanges = ['NIFTY_50', '.INX', '.IXIC']


def get_price():
    prices = []
    for ticker, exchange in zip(tickers, exchanges):
        url = f'https://www.google.com/finance/quote/{exchange}:{ticker}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        class_name = "YMlKec fxKbKc"
        price = float(soup.find(class_=class_name).text.strip()
                      [0:].replace(",", ""))
        prices.append(price)
    return prices


def get_home():
    tickers = ["INDEXNSE", "INDEXBOM", "INDEXSP"]
    exchanges = ['NIFTY_50', 'SENSEX', '.INX']
    prices = []
    for ticker, exchange in zip(tickers, exchanges):
        url = f'https://www.google.com/finance/quote/{exchange}:{ticker}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        class_name = "YMlKec fxKbKc"
        price = float(soup.find(class_=class_name).text.strip()
                      [0:].replace(",", ""))
        prices.append(price)
    return prices


def get_other_data():
    url = f'https://www.google.com/finance/quote/{exchanges[0]}:{tickers[0]}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    class_name = "YMlKec"
    prices = soup.find_all(class_=class_name)
    class_ticker = 'pKBk1e'
    class_perct = "JwB6zf V7hZne"
    value = soup.find_all(class_=class_perct)
    tickers_prices = {}
    tickers_perct = {}
    target_tickers = ["NIFTY 50", "Nifty Bank", "Nifty IT", "SENSEX"]
    for i, price_elem in enumerate(prices):
        price = price_elem.text.strip()
        ticker_elem = price_elem.find_previous('div', class_=class_ticker)
        if ticker_elem and ticker_elem.text.strip() in target_tickers:
            ticker = ticker_elem.text.strip()
            tickers_prices[ticker] = price
    for i, perct_elem in enumerate(value[:4]):
        perct = perct_elem.text.strip()
        ticker_elem = perct_elem.find_previous('div', class_=class_ticker)
        if ticker_elem and ticker_elem.text.strip() in target_tickers:
            ticker = ticker_elem.text.strip()
            tickers_perct[ticker] = perct
    return list(tickers_prices.values()), list(tickers_perct.values()), tickers_prices, tickers_perct

@app.route('/price')
def price():
    prices = get_price()
    unique_prices, unique_perct, tickers_prices, tickers_perct = get_other_data()
    home_price = get_home()
    data = {
        'tickers_prices': tickers_prices,
        'tickers_perct': tickers_perct,
    }
    return jsonify(data=data, prices=prices, unique_prices=unique_prices, unique_perct=unique_perct, home_price=home_price)


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=3020)
