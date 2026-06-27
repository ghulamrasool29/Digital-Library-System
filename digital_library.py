class Book:
    def __init__(self, title, author, book_id, total_copies):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.total_copies = total_copies
        self.available_copies = total_copies
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print("Book Added Successfully!")
    def search_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found")
                print("Title:", book.title)
                print("Author:", book.author)
                print("Book ID:", book.book_id)
                print("Available Copies:", book.available_copies)
                return

        print("Book Not Found")
    def search_by_author(self, author):
        found = False

        for book in self.books:
            if book.author.lower() == author.lower():
                print("\nTitle:", book.title)
                print("Book ID:", book.book_id)
                print("Available Copies:", book.available_copies)
                found = True

        if not found:
            print("No Books Found")
    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:

                if book.available_copies > 0:
                    book.available_copies -= 1
                    print("Book Borrowed Successfully!")
                else:
                    print("No Copies Available")

                return

        print("Book Not Found")
    def return_book(self, book_id):
        for book in self.books:

            if book.book_id == book_id:

                if book.available_copies < book.total_copies:
                    book.available_copies += 1
                    print("Book Returned Successfully!")
                else:
                    print("All Copies Already Returned")

                return

        print("Book Not Found")
    def view_books(self):

        if len(self.books) == 0:
            print("No Books Available")
            return

        print("\n----- All Books -----")

        for book in self.books:
            print("\nTitle:", book.title)
            print("Author:", book.author)
            print("Book ID:", book.book_id)
            print("Available Copies:", book.available_copies)
    def delete_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:
                self.books.remove(book)
                print("Book Deleted Successfully!")
                return

        print("Book Not Found")
library = Library()

while True:

    print("\n===== Digital Library System =====")

    print("1. Add Book")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View All Books")
    print("7. Delete Book")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        title = input("Enter Title: ")
        author = input("Enter Author: ")
        book_id = input("Enter Book ID: ")
        copies = int(input("Enter Total Copies: "))

        book = Book(title, author, book_id, copies)

        library.add_book(book)

    elif choice == "2":

        title = input("Enter Title: ")

        library.search_by_title(title)

    elif choice == "3":

        author = input("Enter Author: ")

        library.search_by_author(author)

    elif choice == "4":

        book_id = input("Enter Book ID: ")

        library.borrow_book(book_id)

    elif choice == "5":

        book_id = input("Enter Book ID: ")

        library.return_book(book_id)

    elif choice == "6":

        library.view_books()

    elif choice == "7":

        book_id = input("Enter Book ID: ")

        library.delete_book(book_id)

    elif choice == "8":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")