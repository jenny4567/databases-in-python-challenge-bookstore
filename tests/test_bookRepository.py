from lib.bookRepository import BookRepository
from lib.book import Book

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_list_all(db_connection):
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    my_book_repo = BookRepository(db_connection)
    all_my_books = my_book_repo.all()
    assert all_my_books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
        ]