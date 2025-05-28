from lib.models import session, Book, Author

def create_author(name):
    author = Author(name=name)
    session.add(author)
    session.commit()
    return author

def create_book(title, year, author_name):
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = create_author(author_name)
    book = Book(title=title, year=year, author=author)
    session.add(book)
    session.commit()
    return book

def list_books():
    return session.query(Book).all()

def list_authors():
    return session.query(Author).all()

def delete_book(title):
    book = session.query(Book).filter_by(title=title).first()
    if book:
        session.delete(book)
        session.commit()
        return True
    return False

def delete_author(name):
    author = session.query(Author).filter_by(name=name).first()
    if author:
        session.delete(author)
        session.commit()
        return True
    return False

def search_books_by_title(keyword):
    return session.query(Book).filter(Book.title.ilike(f"%{keyword}%")).all()

def search_books_by_author(author_name):
    return session.query(Book).join(Author).filter(Author.name.ilike(f"%{author_name}%")).all()