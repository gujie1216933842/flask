from flask import jsonify, request, Blueprint, flash, render_template
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from . import web
from app.view_models.book import *
import json


# 蓝图  buleprint
# web = Blueprint('web', __name__)

@web.route('/book/search')
def search():
    '''
    :param q:
    :param page:
    :return:
    '''
    # print('haha:%s' % (request.args['q']))
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        # return jsonify(form.errors)
        flash('搜索的关键字不符合要求,请重新输入关键字')
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])



@web.route('/save_to_wish')
def save_to_wish():
    pass



@web.route('/test')
def test():
    r = {
        'name': None,
        'age': 18
    }

    r1 = {}

    flash('hello,qiyue', category='error')
    flash('hello,jiuyue', category='warning')

    # 模板
    return render_template('', data=r, data1=r1)
