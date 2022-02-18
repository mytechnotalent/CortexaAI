# pyright: reportMissingImports=false

import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def welcome():
    return jsonify({'status': 'api working'})


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))