from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book("Brave New World")
    library.add_book("1984")

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()
""" 
    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
 """
if __name__ == "__main__":
    main()