class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "available" if self.available else "borrowed"
        return f"{self.title} by {self.author} ({status})"

    __repr__ = __str__


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return self.name

    __repr__ = __str__


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron, book):
        if patron not in self.patrons:
            return False

        if book in self.books and book.available:
            book.available = False
            patron.borrowed_books.append(book)
            return True

        return False

    def return_book(self, patron, book):
        if patron not in self.patrons:
            return False

        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            return True

        return False


if __name__ == "__main__":
    library = Library()

    book = Book("2026", "XYZ")
    patron = Patron("Alice")

    library.add_book(book)
    library.register_patron(patron)

    print("Borrow book:", library.borrow_book(patron, book))
    print("Borrowed books:", patron.borrowed_books)
    print("Return book:", library.return_book(patron, book))
    print("Borrowed books after return:", patron.borrowed_books)
    print("Book status:", book)
