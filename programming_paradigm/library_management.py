class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private by convention

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self._books = []  # Private list of books

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added: {book.title} by {book.author}")
        else:
            print("Only Book instances can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book.title}")
                return
        print(f"No available copy of '{title}' found.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {book.title}")
                return
        print(f"No checked-out copy of '{title}' found.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books available.")

# Example usage
if __name__ == "__main__":
    library = Library()

    b1 = Book("The Hobbit", "J.R.R. Tolkien")
    b2 = Book("1984", "George Orwell")
    b3 = Book("The Hobbit", "J.R.R. Tolkien")  # Duplicate title to test multiple copies

    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)

    library.list_available_books()
    library.check_out_book("The Hobbit")
    library.list_available_books()
    library.return_book("The Hobbit")
    library.list_available_books()
