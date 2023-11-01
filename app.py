import os
from flask import Flask, render_template

app = Flask(__name__)
port = os.environ.get('PORT')


@app.route('/', methods=['GET'])
def home():
    return "home"


@app.route('/placeholder', methods=['GET'])
def placeholder():
    return render_template(
        'index.html', title='Home')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
