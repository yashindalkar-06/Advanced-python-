# Simple Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True   # Book is available by default


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []   # List to store borrowed books


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added to the library.')

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f'Patron "{patron.name}" registered.')

    def borrow_book(self, patron, book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(f'{patron.name} borrowed "{book.title}".')
        else:
            print(f'"{book.title}" is not available.')

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            print(f'{patron.name} returned "{book.title}".')
        else:
            print(f'{patron.name} did not borrow "{book.title}".')


# Driver Code
library = Library()

# Create books
book1 = Book("Python Programming", "Guido van Rossum")
book2 = Book("Data Structures", "Mark Allen Weiss")

# Add books to library
library.add_book(book1)
library.add_book(book2)

# Register patron
patron1 = Patron("Alice")
library.register_patron(patron1)

# Borrow a book
library.borrow_book(patron1, book1)

# Return the book
library.return_book(patron1, book1)