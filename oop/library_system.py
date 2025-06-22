# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize the common attributes of a Book."""
        self.title = title
        self.author = author

    def details(self):
        """Return a string representing the book's details."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the attributes of an EBook, extending Book."""
        super().__init__(title, author)
        self.file_size = file_size

    def details(self):
        """Return a string representing the ebook's details."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the attributes of a PrintBook, extending Book."""
        super().__init__(title, author)
        self.page_count = page_count

    def details(self):
        """Return a string representing the print book's details."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the library with an empty book list."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book.details())
