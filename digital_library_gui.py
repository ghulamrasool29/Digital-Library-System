import tkinter as tk
from tkinter import messagebox, ttk
from digital_library import Book, Library

library = Library()
root = tk.Tk()
root.title("Digital Library System")
root.geometry("1000x700")

heading = tk.Label(
    root,
    text="Digital Library System",
    font=("Arial", 20, "bold")
)
heading.pack(pady=10)

# ---------------- Inputs ----------------

tk.Label(root, text="Book Title").pack()
title_entry = tk.Entry(root, width=40)
title_entry.pack()

tk.Label(root, text="Author").pack()
author_entry = tk.Entry(root, width=40)
author_entry.pack()

tk.Label(root, text="Book ID").pack()
id_entry = tk.Entry(root, width=40)
id_entry.pack()

tk.Label(root, text="Total Copies").pack()
copies_entry = tk.Entry(root, width=40)
copies_entry.pack()

# ---------------- Table ----------------

columns = (
    "Title",
    "Author",
    "Book ID",
    "Available Copies"
)

book_table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=12
)

for col in columns:
    book_table.heading(col, text=col)
    book_table.column(col, width=200)

book_table.pack(pady=20)

# ---------------- Functions ----------------

def refresh_table():

    for row in book_table.get_children():
        book_table.delete(row)

    for book in library.books:

        book_table.insert(
            "",
            "end",
            values=(
                book.title,
                book.author,
                book.book_id,
                book.available_copies
            )
        )

def clear_fields():

    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    copies_entry.delete(0, tk.END)

def add_book():

    try:

        title = title_entry.get()
        author = author_entry.get()
        book_id = id_entry.get()
        copies = int(copies_entry.get())

        book = Book(
            title,
            author,
            book_id,
            copies
        )

        library.add_book(book)

        refresh_table()

        clear_fields()

        messagebox.showinfo(
            "Success",
            "Book Added Successfully"
        )

    except:

        messagebox.showerror(
            "Error",
            "Invalid Input"
        )

def search_title():

    title = title_entry.get()

    found = False

    for book in library.books:

        if book.title.lower() == title.lower():

            messagebox.showinfo(
                "Book Found",
                f"Title: {book.title}\n"
                f"Author: {book.author}\n"
                f"Book ID: {book.book_id}\n"
                f"Available: {book.available_copies}"
            )

            found = True
            break

    if not found:

        messagebox.showerror(
            "Not Found",
            "Book Not Found"
        )

def search_author():

    author = author_entry.get()

    result = ""

    for book in library.books:

        if book.author.lower() == author.lower():

            result += (
                f"{book.title}\n"
                f"Book ID: {book.book_id}\n\n"
            )

    if result:

        messagebox.showinfo(
            "Books Found",
            result
        )

    else:

        messagebox.showerror(
            "Not Found",
            "No Books Found"
        )

def borrow_book():

    book_id = id_entry.get()

    for book in library.books:

        if book.book_id == book_id:

            if book.available_copies > 0:

                book.available_copies -= 1

                refresh_table()

                messagebox.showinfo(
                    "Success",
                    "Book Borrowed Successfully"
                )

            else:

                messagebox.showerror(
                    "Error",
                    "No Copies Available"
                )

            return

    messagebox.showerror(
        "Error",
        "Book Not Found"
    )

def return_book():

    book_id = id_entry.get()

    for book in library.books:

        if book.book_id == book_id:

            if book.available_copies < book.total_copies:

                book.available_copies += 1

                refresh_table()

                messagebox.showinfo(
                    "Success",
                    "Book Returned Successfully"
                )

            else:

                messagebox.showerror(
                    "Error",
                    "All Copies Already Returned"
                )

            return

    messagebox.showerror(
        "Error",
        "Book Not Found"
    )

def delete_book():

    book_id = id_entry.get()

    for book in library.books:

        if book.book_id == book_id:

            library.books.remove(book)

            refresh_table()

            messagebox.showinfo(
                "Success",
                "Book Deleted Successfully"
            )

            return

    messagebox.showerror(
        "Error",
        "Book Not Found"
    )

# ---------------- Buttons ----------------

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Book",
    width=15,
    command=add_book
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Search Title",
    width=15,
    command=search_title
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Search Author",
    width=15,
    command=search_author
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Borrow Book",
    width=15,
    command=borrow_book
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    button_frame,
    text="Return Book",
    width=15,
    command=return_book
).grid(row=1, column=1, padx=5, pady=5)

tk.Button(
    button_frame,
    text="Delete Book",
    width=15,
    command=delete_book
).grid(row=1, column=2, padx=5, pady=5)

root.mainloop()