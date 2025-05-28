from lib.helper import (
    create_book, delete_book, list_books,
    create_author, delete_author, list_authors,
    search_books_by_title, search_books_by_author
)

def main():
    print("Welcome to BookBuddy CLI :books:")
    while True:
        print("\n[1] Add Book  [2] List Books  [3] Delete Book")
        print("[4] Add Author  [5] List Authors  [6] Delete Author")
        print("[7] Search Book by Title  [8] Search Book by Author")
        print("[0] Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Book Title: ")
            year = int(input("Publication Year: "))
            author = input("Author Name: ")
            book = create_book(title, year, author)
            print(f"Added: {book}")
        elif choice == '2':
            for book in list_books():
                print(book)
        elif choice == '3':
            title = input("Title of book to delete: ")
            success = delete_book(title)
            print("Deleted." if success else "Book not found.")
        elif choice == '4':
            name = input("Author Name: ")
            author = create_author(name)
            print(f"Added: {author}")
        elif choice == '5':
            for author in list_authors():
                print(author)
        elif choice == '6':
            name = input("Name of author to delete: ")
            success = delete_author(name)
            print("Deleted." if success else "Author not found.")
        elif choice == '7':
            keyword = input("Enter title keyword: ")
            results = search_books_by_title(keyword)
            for book in results:
                print(book)
        elif choice == '8':
            name = input("Enter author name: ")
            results = search_books_by_author(name)
            for book in results:
                print(book)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")