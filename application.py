from flask import Flask, Response, request, jsonify
from xmlrpc import client
import json
import requests

app = Flask(__name__)

base_url = 'http://localhost:8069'
db = 'bel-20200113'

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/article_list')
def login_article_list():
    username = 'admin@amarbay.com'
    password = '123'
    # print(username + ' pass ' + password)
    params = {
        'db': db,
        'login': username,
        'password': password
    }
    odoo_url = base_url + '/web/session/authenticate'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Content-Length': str(len(json.dumps(params)))
    }

    response = requests.post(url = odoo_url, data= json.dumps({'params': params}) , headers= headers)

    print(response.json())
    # dump(response)
    res_data = response.json()
    sessionId = res_data['result']['session_id']

    url = base_url + '/ecom/product_list_temp'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': 'session_id= %s'%sessionId
    }

    odooResponse = requests.post(url = url, data = json.dumps({'jsonrpc': '2.0', 'method': 'call', 'params': params}) , headers = headers)

    article_data = odooResponse.json()
    # print(today_sale_data)
    article_list = json.loads(article_data['result'])

    return jsonify(article_list)

@app.route('/article_list2')
def login_article_list2():
    username = 'admin@amarbay.com'
    password = '123'
    # print(username + ' pass ' + password)
    params = {
        'db': db,
        'login': username,
        'password': password
    }
    url = base_url + '/ecom/product_list_temp'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Content-Length': str(len(json.dumps(params)))
    }

    odooResponse = requests.post(
        url = url, data = json.dumps({'jsonrpc': '2.0', 'method': 'call', 'params': params}) , headers = headers)

    today_sale_data = odooResponse.json()
    # print(today_sale_data)
    today_sale_list = json.loads(today_sale_data['result'])

    return jsonify(today_sale_list)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(debug=True)
