import json
import os

class Book:
    def __init__(self, title, author, year, genre, read):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read = read

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "read": self.read
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["title"],
            data["author"],
            data["year"],
            data["genre"],
            data["read"]
        )


class LibraryManager:
    def __init__(self, filename="library.txt"):
        self.filename = filename
        self.library = self.load_library()

    def load_library(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        return []

    def save_library(self):
        with open(self.filename, "w") as file:
            json.dump([book.to_dict() for book in self.library], file, indent=4)

    def add_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = int(input("Enter publication year: "))
        genre = input("Enter genre: ")
        read = input("Have you read it? (yes/no): ").strip().lower() == "yes"
        book = Book(title, author, year, genre, read)
        self.library.append(book)
        print("✅ Book added.")

    def remove_book(self):
        title = input("Enter title of the book to remove: ").lower()
        for book in self.library:
            if book.title.lower() == title:
                self.library.remove(book)
                print("✅ Book removed.")
                return
        print("❌ Book not found.")

    def search_books(self):
        keyword = input("Enter title or author to search: ").lower()
        results = [book for book in self.library
                   if keyword in book.title.lower() or keyword in book.author.lower()]
        if results:
            print("\n📚 Search Results:")
            self.display_books(results)
        else:
            print("❌ No matching books found.")

    def display_books(self, books=None):
        books = books if books is not None else self.library
        if not books:
            print("📭 No books found.")
            return
        for i, book in enumerate(books, 1):
            status = "Read" if book.read else "Unread"
            print(f"{i}. {book.title} by {book.author} ({book.year}), {book.genre} - {status}")

    def display_stats(self):
        total = len(self.library)
        if total == 0:
            print("📭 No books to show stats.")
            return
        read_count = sum(book.read for book in self.library)
        percent = (read_count / total) * 100
        print(f"\n📊 Stats:\nTotal books: {total}\nRead: {read_count} ({percent:.2f}%)")

    def run(self):
        while True:
            print("\n📘 Personal Library Menu")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_books()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.display_stats()
            elif choice == "6":
                self.save_library()
                print("📂 Library saved. Goodbye!")
                break
            else:
                print("❌ Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    manager = LibraryManager()
    manager.run()
