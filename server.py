from flask import Flask, request, jsonify
import json
import requests
import os

app = Flask(__name__)
port = int(os.environ["PORT"])
# port = '5000'

@app.route('/', methods=['POST'])
def index():
 
  

  cont = 'Your Order ' + str(contact_id) + ' will be delivered on Monday, 27th of March.'

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': cont 
      #'content': 'The price of %s is %f BTC and %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD'])
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port, host="0.0.0.0")
#  app.run(port=port)
