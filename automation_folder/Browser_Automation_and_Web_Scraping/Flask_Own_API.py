from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(rate[:-4])

    return rate

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>Welcome to Flask Own API!</h1>'
            '<br>'
            '<h2>Currency Rate API</h2>'
            '<h3>Example URL: api/v1/usd-eur</h3>')

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    result_dicionary = {
        'in_currency': in_cur,
        'out_currency': out_cur,
        'rate': rate,
    }
    return jsonify(result_dicionary)



app.run(host='0.0.0.0', port=5000)
