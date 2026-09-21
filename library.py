import json
import os


# Book class
class Book:
    def __init__(self, book_id, title, author, issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = issued

    def to_dict(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "issued": self.issued
        }


# Library class
class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename

        # List to store Book objects
        self.books = []

        # Dictionaries for quick lookup
        self.books_by_id = {}
        self.books_by_title = {}
        self.books_by_author = {}

        self.load_books()

    # Add book to lookup dictionaries
    def add_to_lookup(self, book):
        self.books_by_id[book.book_id] = book

        title = book.title.lower()
        author = book.author.lower()

        if title not in self.books_by_title:
            self.books_by_title[title] = []

        if author not in self.books_by_author:
            self.books_by_author[author] = []

        self.books_by_title[title].append(book)
        self.books_by_author[author].append(book)

    # Load books from JSON file
    def load_books(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)

                for item in data:
                    book = Book(
                        item["id"],
                        item["title"],
                        item["author"],
                        item["issued"]
                    )

                    self.books.append(book)
                    self.add_to_lookup(book)

            except (json.JSONDecodeError, FileNotFoundError):
                print("Could not load book data.")

    # Save books to JSON file
    def save_books(self):
        data = [book.to_dict() for book in self.books]

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Add a new book
    def add_book(self):
        print("\n--- Add Book ---")

        book_id = input("Enter Book ID: ").strip()

        if not book_id:
            print("Book ID cannot be empty.")
            return

        if book_id in self.books_by_id:
            print("Book ID already exists.")
            return

        title = input("Enter Book Title: ").strip()

        if not title:
            print("Title cannot be empty.")
            return

        author = input("Enter Author Name: ").strip()

        if not author:
            print("Author cannot be empty.")
            return

        book = Book(book_id, title, author)

        self.books.append(book)
        self.add_to_lookup(book)
        self.save_books()

        print("Book added successfully.")

    # Search books
    def search_book(self):
        print("\n--- Search Book ---")

        keyword = input(
            "Enter title or author to search: "
        ).strip().lower()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        results = []

        # Search through list
        for book in self.books:
            if (keyword in book.title.lower()
                    or keyword in book.author.lower()):
                results.append(book)

        if not results:
            print("No books found.")
            return

        print("\nSearch Results")
        print("-" * 75)
        print(f"{'ID':<10}{'Title':<30}{'Author':<20}{'Status':<10}")
        print("-" * 75)

        for book in results:
            status = "Issued" if book.issued else "Available"

            print(
                f"{book.book_id:<10}"
                f"{book.title:<30}"
                f"{book.author:<20}"
                f"{status:<10}"
            )

        print("-" * 75)

    # Issue a book
    def issue_book(self):
        print("\n--- Issue Book ---")

        book_id = input("Enter Book ID: ").strip()

        if book_id not in self.books_by_id:
            print("Book not found.")
            return

        book = self.books_by_id[book_id]

        if book.issued:
            print("This book is already issued.")
            return

        book.issued = True
        self.save_books()

        print(f"Book '{book.title}' issued successfully.")

    # Return a book
    def return_book(self):
        print("\n--- Return Book ---")

        book_id = input("Enter Book ID: ").strip()

        if book_id not in self.books_by_id:
            print("Book not found.")
            return

        book = self.books_by_id[book_id]

        if not book.issued:
            print("This book is already available.")
            return

        book.issued = False
        self.save_books()

        print(f"Book '{book.title}' returned successfully.")

    # Display all books
    def list_books(self):
        print("\n--- All Books ---")

        if not self.books:
            print("No books available.")
            return

        print("-" * 75)
        print(f"{'ID':<10}{'Title':<30}{'Author':<20}{'Status':<10}")
        print("-" * 75)

        for book in self.books:
            status = "Issued" if book.issued else "Available"

            print(
                f"{book.book_id:<10}"
                f"{book.title:<30}"
                f"{book.author:<20}"
                f"{status:<10}"
            )

        print("-" * 75)

    # Library report
    def report(self):
        total_books = len(self.books)

        issued_books = 0

        for book in self.books:
            if book.issued:
                issued_books += 1

        available_books = total_books - issued_books

        print("\n--- Library Report ---")
        print("-------------------------")
        print(f"Total Books     : {total_books}")
        print(f"Issued Books    : {issued_books}")
        print(f"Available Books : {available_books}")
        print("-------------------------")


# Main program
def main():

    library = Library()

    while True:

        print("\n================================")
        print("   LIBRARY BOOK INVENTORY")
        print("================================")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. List All Books")
        print("6. Library Report")
        print("7. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.search_book()

        elif choice == "3":
            library.issue_book()

        elif choice == "4":
            library.return_book()

        elif choice == "5":
            library.list_books()

        elif choice == "6":
            library.report()

        elif choice == "7":
            print("Thank you for using the Library System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start program
if __name__ == "__main__":
    main()