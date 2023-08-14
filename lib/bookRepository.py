from lib.book import Book

class BookRepository():
    # Initialise connection
    def __init__(self, connection):
        self._connection = connection

    '''
    All method to return all books in bookstore.
    '''
    def all(self):
        # Executes the SQL query:
        # SELECT id, title, author FROM book_store;
        # Returns all books in the bookstore   
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books  
