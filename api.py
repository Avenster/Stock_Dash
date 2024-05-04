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
    print(price)
    return price

@app.route('/price')
def price():
    price = get_price()
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True, threaded=True,port=3010)
    while True:
        time.sleep(10)
