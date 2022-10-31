from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '0.0.0.0'}})


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    info = {'slackUsername': 'OlaJosh',
            'backend': True,
            'Age': 28,
            'Bio': 'I love writing functional codes on the backend'}
    return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True)
