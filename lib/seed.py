from lib.helper import create_book

sample_books = [
    ("Pride and Prejudice", 1813, "Jane Austen"),
    ("1984", 1949, "George Orwell"),
    ("Moby Dick", 1851, "Herman Melville"),
    ("To Kill a Mockingbird", 1960, "Harper Lee"),
    ("The Great Gatsby", 1925, "F. Scott Fitzgerald")
]

for title, year, author in sample_books:
    create_book(title, year, author)

print("Seeded classic book data!")