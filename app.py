import ccxt
import time
from flask import Flask, jsonify

app = Flask(__name__)

OKX_API_KEY = "9eeabb34-7afe-410c-8a07-0aa71ddc49eb"
OKX_SECRET_KEY = "83BC9502DE34D44E5027A40A28EEE336"
OKX_PASSPHRASE = "Ylh20011027@"

exchange = ccxt.okx({
'apiKey': OKX_API_KEY,
'secret': OKX_SECRET_KEY,
'password': OKX_PASSPHRASE,
'enableRateLimit': True,
})

prices = {}

@app.route('/')
def home():
return "<h1>OKX Paper Trading - Loading...</h1>"

@app.route('/api/test')
def test():
try:
ticker = exchange.fetch_ticker('BTC-USDT-SWAP')
return {'price': float(ticker['last']), 'status': 'ok'}
except Exception as e:
return {'error': str(e)}

if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)
