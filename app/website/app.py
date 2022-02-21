# Copyright: (c) 2021, My Techno Talent <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# pyright: reportMissingImports=false

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.htm')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)