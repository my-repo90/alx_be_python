#   base class (Book)
class Book:
    def __init__(self , title:str , author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

#   derived classes (EBook & PrintBook)
#   both classes inherit from Book
class EBook(Book):
    def __init__(self, title, author , file_size:int):
        super().__init__(title, author)
        #   additional attribute (file_size)
        self.file_size = file_size

    def __str__(self):
        return super().__str__()

class PrintBook(Book):
    def __init__(self, title, author , page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return super().__str__()

class Library:
    def __init__(self , books = None):
        if books is None:
            self.books = []
        else:
            self.books = books
        
    #   Adds a Book, EBook, or PrintBook instance to the library
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(self.books)
       