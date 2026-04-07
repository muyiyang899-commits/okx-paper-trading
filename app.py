from flask import Flask, jsonify
import ccxt

app = Flask(__name__)

@app.route('/')
def home():
return jsonify({'status': 'OK', 'msg': 'OKX Paper Trading Bot Running'})

@app.route('/api/price')
def price():
ex = ccxt.okx()
t = ex.fetch_ticker('BTC-USDT')
return jsonify({'btc': t['last']})

if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)
