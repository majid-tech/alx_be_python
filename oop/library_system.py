class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    
class EBook(Book):
    def __init__(self, title, author, file_size: int):
        self.file_size = file_size
        super().__init__(title, author)


class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f'{book.title} by {book.author}')


