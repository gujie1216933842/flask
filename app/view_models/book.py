class BookViewModel(object):
    @classmethod
    def package_sing(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collect(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': [cls.__cut_book_data(data)  for book in data['book']]
        }
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image'],

        }
