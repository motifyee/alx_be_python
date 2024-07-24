
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author}"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}"


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for b in self.books:
            print(b)
