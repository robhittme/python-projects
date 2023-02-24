from markupsafe import escape 
from flask import Flask, jsonify, make_response, request
from db import getEntries 

app = Flask(__name__)

@app.route('/welcome', methods=['POST'])
def welcome():
    content = request.get_json(silent=True, force=True) 

    try:
        data = getEntries()
        return make_response(jsonify(data), 200)
    
    except Exception as ex:
        response = { 'error': 'name is required' }
        return make_response(jsonify(response), 400)

@app.route('/<path:path>', methods=['GET', 'POST'])
def not_found(path):
    response = {'error': 'route not found'}
    return make_response(jsonify(response), 404)


