from flask import Flask
from flask import request
from flask import jsonify

from easytypeahead.core.search_tree import TrieTreeIndex


def init_index():
    print('init the Trie Tree index')
    index_tree = TrieTreeIndex()
    # FIXME: load from storage
    index_tree.add_term('abc', 10)
    index_tree.add_term('abstract', 5)
    index_tree.add_term('apple', 100)
    index_tree.add_term('alpine', 98)
    index_tree.add_term('app', 1000)
    index_tree.add_term('application', 99)
    index_tree.build_tops()
    return index_tree


def create_app():
    return Flask(__name__), init_index()


app, index = create_app()


@app.route('/')
def default():
    return 'Easy Type Ahead is alive!'


# /suggest?t={search_term}
@app.route('/suggest')
def suggest():
    search_term = request.args.get('t', '')
    search_term = search_term.strip()
    print('search:%s' % search_term)
    result = index.search(search_term)
    return jsonify(result)
