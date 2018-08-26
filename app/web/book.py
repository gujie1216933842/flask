from flask import jsonify, request
from fisher import app
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.book import SearchForm


# 蓝图  buleprint

@app.route('/book/search/')
def search(q, page):
    '''
    :param q:
    :param page:
    :return:
    '''

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_isbn(q)
        else:
            result = YuShuBook.search_keyword(q)

        return jsonify(result)

    else:
        return jsonify({'msg': '参数失败'})
