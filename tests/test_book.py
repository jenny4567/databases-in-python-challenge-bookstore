from lib.book import Book

"""
Artist constructs with id, title and author
"""
def test_book_construction():
    my_book = Book(12,"Hogfather", "Terry Pratchett")
    assert my_book.book_id == 12
    assert my_book.title == "Hogfather"
    assert my_book.author == "Terry Pratchett"


"""
We can format Book objects to strings nicely
"""
def test_book_format():
    my_book = Book(12,"Hogfather", "Terry Pratchett")
    assert str(my_book) == "Book 12 - Hogfather by Terry Pratchett"