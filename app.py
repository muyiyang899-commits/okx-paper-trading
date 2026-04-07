from flask import Flask, jsonify
import ccxt

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

@app.route('/')
def home():
return "<h1>OKX Paper Trading - OK!</h1>"

if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)