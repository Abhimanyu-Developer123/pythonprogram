class Library:
    def __init__(self, name):
        self.name = name  # Name of the library
        self.books = {}  # Dictionary to store books and their quantities

    def add_book(self, book_name, quantity=1):  # Add books to the library
        if book_name in self.books:
            self.books[book_name] += quantity
        else:
            self.books[book_name] = quantity
        print(f"Added {quantity} copies of '{book_name}' to the library.")

    def issue_book(self, book_name):  # Issue a book to a user
        if book_name in self.books and self.books[book_name] > 0:
            self.books[book_name] -= 1
            print(f"'{book_name}' has been issued.")
        elif book_name in self.books:
            print(f"'{book_name}' is currently unavailable.")
        else:
            print(f"'{book_name}' does not exist in the library.")

    def return_book(self, book_name):  # Return a book to the library
        if book_name in self.books:
            self.books[book_name] += 1
            print(f"'{book_name}' has been returned.")
        else:
            self.books[book_name] = 1
            print(f"'{book_name}' has been added to the library as a new book.")

    def view_inventory(self):  # Display all books and their quantities
        print(f"\n--- {self.name} Library Inventory ---")
        if not self.books:
            print("No books are currently available in the library.")
        else:
            for book, quantity in self.books.items():
                print(f"{book}: {quantity} copies")

# Example Usage
library = Library("City Central Library")

library.add_book("The Great Gatsby", 5)
library.add_book("1984", 3)
library.add_book("To Kill a Mockingbird", 2)

library.view_inventory()

library.issue_book("1984")
library.issue_book("The Great Gatsby")
library.issue_book("The Alchemist")  # Book not in the library

library.view_inventory()

library.return_book("1984")
library.return_book("The Alchemist")  # Returning a new book

library.view_inventory()