from flask import jsonify, request, Blueprint
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from . import web
from app.view_models.book import *


# 蓝图  buleprint
# web = Blueprint('web', __name__)

@web.route('/book/search')
def search():
    '''
    :param q:
    :param page:
    :return:
    '''
    print('haha:%s' % (request.args['q']))
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_isbn(q)
            result = BookViewModel.package_sing(result, q)
        else:
            result = YuShuBook.search_keyword(q, page)
            result = BookViewModel.package_collect(result, q)

        return jsonify(result)

    else:
        return jsonify(form.errors)
