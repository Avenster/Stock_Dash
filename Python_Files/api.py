from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

tickers = ['INDEXNSE', 'INDEXSP','INDEXNASDAQ']
exchanges = ['NIFTY_50','.INX', '.IXIC']


def get_price():
    prices = []
    for ticker, exchange in zip(tickers, exchanges):
        url = f'https://www.google.com/finance/quote/{exchange}:{ticker}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        class_name = "YMlKec fxKbKc"  
        price = float(soup.find(class_=class_name).text.strip()[0:].replace(",", ""))
        prices.append(price)
    return prices

def get_home():
    tickers = ["INDEXNSE","INDEXBOM","INDEXSP"]
    exchanges = ['NIFTY_50','SENSEX','.INX']
    prices = []
    for ticker, exchange in zip(tickers, exchanges):
        url = f'https://www.google.com/finance/quote/{exchange}:{ticker}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        class_name = "YMlKec fxKbKc"  
        price = float(soup.find(class_=class_name).text.strip()[0:].replace(",", ""))
        prices.append(price)
    return prices

def get_other_data():
    url = f'https://www.google.com/finance/quote/{exchanges[0]}:{tickers[0]}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    class_name = "YMlKec" 
    prices = soup.find_all(class_=class_name)

    class_perct = "JwB6zf V7hZne"
    value = soup.find_all(class_=class_perct)

    unique_prices = set()
    unique_perct = set()

    for i in range(8):
        if i < len(prices):
            price = prices[i].text.strip()
            unique_prices.add(price)
        if i < len(value) and i < 4:
            perct = value[i].text.strip()
            unique_perct.add(perct)

    return list(unique_prices), list(unique_perct)


@app.route('/price')
def price():
    prices = get_price()
    unique_prices, unique_perct = get_other_data()
    home_price = get_home()
    data = {'prices': prices, 'unique_prices': unique_prices, 'unique_perct': unique_perct,'home_price':home_price}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=3020)
