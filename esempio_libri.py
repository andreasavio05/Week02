# ESEMPIO LIBRI
# Demonstrating the use of classes, e.g., defining class Book

# The class describes the structure of a book, with its attributes

class Book:
    def __init__(self, t, a, n): # Parameters to initialize the book instance (object)
        self.title = t # These variables store values of attributes for a real book
        self.author = a
        self.num_pages = n

# There is no real book yet (no instance), only their structure (abstraction)

# Starting from the Book class, it is possible to create a Book instance (reification),
# passing as arguments to function init() the values each attribute has to assume

book1 = Book("Il nome della rosa", "U. Eco", 800)

# Printing a Book variable as done below the memory reference is printed, not object content

print(book1)

# To print object content it is necessary to access object's attributes with the dot notation .

print(book1.title, book1.author, book1.num_pages)

# With the code that follows, another (different) instance (book) is created, with different information

book2 = Book("I pilastri della terra", "K. Follet", 1000)

print(book2.title, book2.author, book2.num_pages)

interi = [5, 7, 9]
stringa = 'abc'

# as much as i can create containers (lists...) of primitive/elementary data like int or str
# i can also create containers of other types of data, like books

books = [book1]
books.append(book2)

for book in books:
    print(book.title, book.author, book.num_pages)



