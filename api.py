from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

ticker = 'INDEXNSE'  
exchange = 'NIFTY_50' 
url = f'https://www.google.com/finance/quote/{exchange}:{ticker}'

def get_price():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    class_name = "YMlKec fxKbKc"  # Class name for the price
    price = float(soup.find(class_=class_name).text.strip()[0:].replace(",", ""))
    return price

def get_other_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    class_name = "YMlKec"  # Class name for the price
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
    price = get_price()
    unique_prices, unique_perct = get_other_data()
    data = {'price': price, 'unique_prices': unique_prices, 'unique_perct': unique_perct}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=3020)
    while True:
        time.sleep(10)
