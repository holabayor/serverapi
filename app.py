import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import enum
import json


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    info = {'slackUsername': 'OlaJosh',
            'backend': True,
            'age': 28,
            'bio': 'I love writing functional codes on the backend'}
    return jsonify(info)

@app.route('/calculate', methods=['POST'], strict_slashes=False)
def operation():
    data = request.get_json()
    x = int(data.get('x'))
    y = int(data.get('y'))
    operator_type = data.get('operator_type')
    if operator_type in ('+', 'addition', 'add', 'plus'):
        result = x + y
    if operator_type in ('-', 'subtraction', 'subtract', 'minus'):
        result = x - y
    if operator_type in ('*', 'multiplication', 'multiply'):
        result = x * y

    info = {'slackUsername': 'OlaJosh',
            'operation_type': operator_type,
            'result': result}
    return jsonify(info)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=int(os.environ.get('PORT', 5000)),
            debug=True)
