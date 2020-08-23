import json

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def default():
    return 'Easy TypeAhead is alive!'


@app.route('/suggest')
def suggest():
    term = request.args.get('term', '')

    print('search:%s' % term)
    # TODO use search tree to search
    return json.dumps(['ab', 'abc', 'abcd'])
