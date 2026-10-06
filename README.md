# 📚 Library Book Inventory Manager

A simple **command-line Library Book Inventory Manager built with Python**. The project allows users to add, search, issue, return, and view books while storing book information in a JSON file for persistent data storage.



## 📌 Features

* Add new books
* Search books by title or author
* Issue books
* Return books
* View all books
* Generate a library report
* Track book availability
* Prevent duplicate Book IDs
* Validate basic user input
* Store and reload book data using JSON
* Use dictionaries for quick book lookup
* Use classes for object-oriented programming

## 🛠️ Technologies Used

* **Python 3**
* **JSON**
* Python built-in libraries:

  * `json`
  * `os`

No external packages are required.

## 📂 Project Structure

```text
Library-Book-Inventory-Manager/
│
├── library.py
├── books.json
└── README.md
```

### `library.py`

Contains the main application logic, including the `Book` and `Library` classes and the menu system.

### `books.json`

Stores the book information so that the data remains available even after the program is closed.



## 💻 Main Menu

When the program starts, it displays the following menu:

```text
================================
   LIBRARY BOOK INVENTORY
================================
1. Add Book
2. Search Book
3. Issue Book
4. Return Book
5. List All Books
6. Library Report
7. Exit
================================
```

The user can select an option to perform the required library operation.

## 📖 Sample Book Data

The project initially contains three sample books:

| ID | Title   | Author | Status    |
| -- | ------- | ------ | --------- |
| 1  | Love    | XYZ    | Available |
| 2  | Hate    | ABC    | Available |
| 3  | Promise | EFG    | Available |

The data is stored in `books.json`:

```json
[
    {
        "id": "1",
        "title": "Love",
        "author": "XYZ",
        "issued": false
    },
    {
        "id": "2",
        "title": "Hate",
        "author": "ABC",
        "issued": false
    },
    {
        "id": "3",
        "title": "Promise",
        "author": "EFG",
        "issued": false
    }
]
```

## 🧩 Object-Oriented Programming

The project uses two main classes.

### `Book` Class

The `Book` class represents an individual book.

Each book contains:

* Book ID
* Title
* Author
* Issued status

Example:

```python
book = Book("1", "Love", "XYZ")
```

The `to_dict()` method converts a Book object into a dictionary so it can be stored in the JSON file.

### `Library` Class

The `Library` class manages the collection of books and provides functions for:

* Adding books
* Searching books
* Issuing books
* Returning books
* Listing books
* Generating reports
* Loading data
* Saving data

## 🗂️ Data Structures Used

The project demonstrates different Python data structures.

### List

A list stores all `Book` objects:

```python
self.books = []
```

### Dictionaries

Dictionaries are used for quick lookup:

```python
self.books_by_id = {}
self.books_by_title = {}
self.books_by_author = {}
```

This provides a HashMap-like approach for organizing and finding books efficiently.

## 💾 JSON Data Persistence

The application uses `books.json` to save book information.

Whenever a book is:

* Added
* Issued
* Returned

the updated information is saved to the JSON file.

When the program starts again, the `load_books()` function reads the JSON file and restores the stored book data.

This means the book information is **not lost when the program is closed**.

## 🔍 Search Function

Users can search for books using a title or author name.

For example:

```text
--- Search Book ---
Enter title or author to search: love

Search Results
---------------------------------------------------------------------------
ID        Title                         Author              Status
---------------------------------------------------------------------------
1         Love                          XYZ                 Available
---------------------------------------------------------------------------
```

The search is case-insensitive, so entering `love`, `Love`, or `LOVE` can find the same book.

## 📊 Library Report

The program provides a simple report showing:

* Total number of books
* Number of issued books
* Number of available books

Example:

```text
--- Library Report ---
-------------------------
Total Books     : 3
Issued Books    : 1
Available Books : 2
-------------------------
```

## ⚠️ Error Handling

The application handles several common situations.

### Duplicate Book ID

```text
Book ID already exists.
```

### Book Not Found

```text
Book not found.
```

### Already Issued

```text
This book is already issued.
```

### Already Returned

```text
This book is already available.
```

### Empty Input

The program prevents empty Book IDs, titles, authors, and search keywords.

## 🎯 Learning Objectives

Through this project, I practiced:

* Object-Oriented Programming (OOP)
* Python classes and objects
* Lists and dictionaries
* Iteration and conditional statements
* Functions and methods
* JSON file handling
* Data persistence
* Searching and filtering
* Basic error handling
* Command-line application development
* Organizing a Python project into reusable components

## 🚀 Future Improvements

Possible improvements for this project include:

* Add a graphical user interface using Tkinter
* Add member/student management
* Track who borrowed each book
* Add borrowing and return dates
* Add book deletion and editing
* Add advanced search and filtering
* Add automated unit tests
* Add a database such as SQLite or MySQL
* Add authentication for library staff

## 👨‍💻 Author

Anamika Dhakal

BICTE | Python Programmer

---

⭐ This project was developed as part of my Python programming project series.
