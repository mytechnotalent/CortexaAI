# Copyright: (c) 2021, My Techno Talent <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# pyright: reportMissingImports=false

import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def welcome():
    return jsonify({'status': 'api working'})


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))