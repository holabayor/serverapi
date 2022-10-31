import os
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    info = {'slackUsername': 'OlaJosh',
            'backend': True,
            'age': 28,
            'bio': 'I love writing functional codes on the backend'}
    return jsonify(info)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=int(os.environ.get('PORT', 5000)),
            debug=True)
