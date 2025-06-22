# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize the common attributes of a Book."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for printing Book details."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook attributes, call Book's init."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for printing EBook details."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook attributes, call Book's init."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for printing PrintBook details."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books using __str__."""
        for book in self.books:
            print(book)

