from flask import Flask, request, jsonify # Exports the flask library
app = Flask(__name__) # Single module that grabs all modules executing from this file

@app.route('/', methods=['GET'])
def index_page():
    response = jsonify('Hello World!!!')
    response.status_code = 200
    return response

@app.route('/transactions/', methods=['GET'])
def list_of_transactions():
    response = jsonify({'balance': 0, 
    'transactions': [ 
        {'amount': 0.0, 'current_balance': 230, 'description': 'blue jean', 'id':2, 'inital_balance': 300, 'time': "2019-01-12 09:00:00", 'type': 'expense'}
    ]})
    response.status_code = 200
    return response

@app.route('/login', methods=['GET', 'POST']) # HTTP request methods namely "GET" or "POST"
def login():
    data = []
    if request.method == 'POST': # Checks if it's a POST request
        data = [dict(id='1', name='max', email='max@gmail.com')] # Data structure of JSON format
        response = jsonify(data) # Converts your data strcuture into JSON format
        response.status_code = 202 # Provides a response status code of 202 which is "Accepted" 

        return response # Returns the HTTP response
    else:
        data = [dict(id='none', name='none', enmail='none')] # Data structure of JSON format
        response = jsonify(data) # Converts your data strcuture into JSON format
        response.status_code = 406 # Provides a response status code of 406 which is "Not Acceptable"

        return response # Returns the HTTP response

