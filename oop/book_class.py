class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        print(f"Deleting {self.title}")

# Creating the book object (title must be in quotes)
book = Book('1984', "George Orwell", 1949)

# Using __str__
print(book)        # Output: '1984' by George Orwell (1949)

# Using __repr__
print(repr(book))  # Output: Book('1984', 'George Orwell', 1949)

# Deleting the object
del book           # Output: Deleting 1984
