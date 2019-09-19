from flask import Flask, request, jsonify
import json
import requests
import os

app = Flask(__name__)
port = int(os.environ["PORT"])
# port = '5000'

@app.route('/', methods=['POST'])
def index():
  data = json.loads(request.get_data())

  # FETCH THE CRYPTO NAME
  contact_id = data['conversation']['memory']['contract']['raw']

  # FETCH BTC/USD/EUR PRICES
  #r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")
  
  headers = {'content-type': 'application/json'}
  # headers = { 'Authorization' : 'Token ' + token }
  aa = str(133)
  r = requests.get("https://my307428.crm.ondemand.com/sap/c4c/odata/v1/contract/ContractCollection?$filter=ID%20eq%20%27" + contact_id + "%27&$format=json", auth=('mpospisil', 'Oblacek123'), json={"key": "value"})

  #ss = r.json()
  #json_data = json.loads(r.text)
  aa = r.text.find('ProcessingTypeCode')
  bbb = r.text[int(aa + 21): int(aa + 26)]
  aaa = r.json() # ["BuyerPartyMainContactPartyID"]
  
  cont = 'Contract ' + str(contact_id) + ' does not exist in the System, can you try again?'
  if bbb == 'SRCO':
    cont = 'Processing type of your Contract ' + str(contact_id) + ' is ' + str(bbb) + '.'

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'Processing type of your Contract ' + str(contact_id) + ' is ' + str(bbb) + '.'
      #'content': 'The price of %s is %f BTC and %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD'])
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port, host="0.0.0.0")
#  app.run(port=port)
