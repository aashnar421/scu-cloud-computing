from flask import Flask
from flask import render_template
import requests
import os

app = Flask(__name__)


API_HOST = os.getenv('API_HOST')
API_PORT = os.getenv('API_PORT')
API_ENDPOINT = os.getenv('API_ENDPOINT')


@app.route('/')
def get_meal():
    api_url = f'http://{API_HOST}:{API_PORT}/{API_ENDPOINT}'

    # print(api_url) => http://api:5000/get_meal

    response = requests.get(api_url)

    jsonData = response.json()

    return render_template('index.html', meal_name=jsonData['name'], meal_price=jsonData['price'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
