class Book():
    # Initialise with empty id, title and author
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    '''
    A method to make it look nicer when we print a book.
    '''
    def __repr__(self):
        # Return string representation of id, Book title and author.
        return f"Book {self.book_id} - {self.title} by {self.author}"