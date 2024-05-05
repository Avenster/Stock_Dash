from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app) 

@app.route('/api/news')
def get_news():
    url = "https://news.google.com/search?q=sp500&hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    class_JtKRv_elements = soup.find_all(class_="JtKRv")
    class_Quavad_elements = soup.find_all(class_="Quavad")
    
    news_data = {
        "JtKRv": [element.text for element in class_JtKRv_elements[:10]],
        "Quavad": [f"https://news.google.com{element.get('src')}" if element.get('src') else None for element in class_Quavad_elements[:10]]
    }
    
    return jsonify(news_data)

@app.route('/api/image')
def get_image():
    url = request.args.get('url')
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            
            jpeg_image = BytesIO()
            image.save(jpeg_image, format='JPEG')
            jpeg_image.seek(0)
            print(jpeg_image)
            
            return send_file(jpeg_image, mimetype='image/jpeg')
    
    return 'Image not found', 404

if __name__ == '__main__':
    app.run(debug=True)
