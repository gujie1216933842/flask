from flask import jsonify
from fisher import app
from helper import is_isbn_or_key
from yushu_book import YuShuBook


# 蓝图  buleprint

@app.route('/book/search/<q>/<page>')
def search(q, page):
    '''
    :param q:
    :param page:
    :return:
    '''
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_isbn(q)
    else:
        result = YuShuBook.search_keyword(q)

    return jsonify(result)
