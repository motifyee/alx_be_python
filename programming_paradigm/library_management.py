class Book:
    _is_checked_out = False

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        idx = [x.title for x in self._books].index(title)
        # self._books.pop(idx)
        self._books[idx]._is_checked_out = True

    def return_book(self):
        idx = [x.title for x in self._books].index(0)
        return self._books[idx]

    def list_available_books(self):
        for t in [x.title for x in self._books]:
            if not t._is_checked_out:
                print(t)
