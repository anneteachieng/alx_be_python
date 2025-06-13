# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book):
        """Adds a new Book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Returns a book by title if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' is not currently checked out.")

    def list_available_books(self):
        """Prints all books that are currently available for checkout."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
        else:
            for book in available:
                print(book)

