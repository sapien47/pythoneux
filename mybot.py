from flask import Flask, request, jsonify
import json
import requests
import os




app = Flask(__name__)

port = int(os.environ["PORT"])
print(port)
@app.route('/', methods=['POST'])
def index():
    data = json.loads(request.get_data())
    print(json.loads(request.get_data()))
    crypto_name = data['conversation']['memory']['crypto']['raw']
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=" + crypto_name + "&tsyms=BTC,USD,EUR")

    return jsonify(
        status=200,
        replies=[{
            'type': 'text',
            'content': 'The price of %s is %f BTC and %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD']),
        }],
        conversation={
            'memory': {'key': 'value'}
        }
    )
@app.route('/errors', methods=['POST'])
def errors():
    print(json.loads(request.get_data()))
    return jsonify(status=200)


app.run(port=port, host="0.0.0.0")
