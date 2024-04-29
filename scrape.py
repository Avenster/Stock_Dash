from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import threading
import time

app = Flask(__name__)

url = 'https://www.coindesk.com/price/bitcoin/'
class_name = "currency-pricestyles__Price-sc-1v249sx-0 fcfNRE"
current_price = None

def scrape_price():
    global current_price
    while True:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            price_element = soup.find(class_=class_name)
            if price_element:
                current_price = price_element.get_text()
            else:
                current_price = None
        except Exception as e:
            print("Error while scraping:", e)
        time.sleep(1)  # Update every second

# Start a background thread to continuously scrape the price
scraping_thread = threading.Thread(target=scrape_price)
scraping_thread.daemon = True
scraping_thread.start()

@app.route('/bitcoin_price')
def bitcoin_price():
    global current_price
    if current_price:
        return jsonify({'price': current_price})
    else:
        return jsonify({'error': 'Failed to fetch price'})

if __name__ == '__main__':
    app.run(debug=True)
