from app.libs.helper import HTTP
from flask import current_app


class YuShuBook():
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyworf_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_keyword(cls, keyword, page=1):
        url = cls.keyworf_url.format(keyword, cls.per_page, cls.calulate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calulate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
