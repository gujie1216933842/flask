class BookViewModel(object):
    def package_sing(self, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keywords': keyword
        }
        if data:
            returned['total'] = 1

    def package_collect(self):
        pass

    def __cut_book_data(self, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image'],

        }
