class LibraryBook:
    '''This class represents a book in the library.'''
    
    def __init__(self, book, author, uniqueid): 
        '''Initialize a book with its title, author, and unique ID.'''
        self.book = book
        self.author = author
        self.uniqueid = uniqueid

class LibrarySystem: 
    '''This class represents the library system.'''
    
    def __init__(self):
        self.books = []

    def addbook(self, book):
        '''Add a book to the library.'''
        self.books.append(book)

    def removebook(self, book):
        '''Remove a book from the library.'''
        try:
            self.books.remove(book)
            print(f"Book '{book.book}' removed successfully!")
        except ValueError:
            print("Book not found!")

    def searchauthors(self, author):
        '''Search for books by a given author.'''
        written_by_author = []
        for book in self.books:
            if book.author == author:
                written_by_author.append(book)
        return written_by_author

    def searchname(self, book_title):
        '''Search for a book by its title.'''
        for book in self.books:
            if book.book == book_title:
                return book

    def searchbookuniqueid(self, uniqueid):
        '''Search for a book by its unique ID.'''
        for book in self.books:
            if book.uniqueid == uniqueid:
                return book

    def librarycatalog(self):
        '''Get the library catalog.'''
        return self.books

'''generating a function to be the main menu in the user-interface program while generating a lib to represent the library system'''
def main():
    lib = LibrarySystem()  

    print("=====================")
    print("Welcome to freeliby")
    print("=====================")
    #printing the header of the main menu in the user-interface program
    
    '''generating a new while loop as a main menu of the library system in form of an infinite loop until the users choose to exit the system'''    
    while True:
        print("Choose an option below")
        print("1. Adding new books")
        print("2. Search a book by book title")
        print("3. Search a book by author")
        print("4. Removing a book")
        print("5. Library catalog")
        print("6. Exit")
    
        try:
            option = int(input("Enter option here: "))
        except ValueError:
            print("Your input is invalid. Please type an integer number as your input")
            continue
        #generating the system for the users to input the options they would like to do in the system/program 

        ''' creating list of if, elifs, and else statements as a part of the while loop 
        to ensure the program will responds to the user's input accordingly. '''
        if option == 1:
            book_title = input("Enter book title: ")
            author = input("Enter author: ")
            uniqueid = input("Enter unique ID: ")
            book = LibraryBook(book_title, author, uniqueid)
            lib.addbook(book)
            print("Book added successfully!")

        elif option == 2:
            book_title = input("Type the book title: ")
            found_book = lib.searchname(book_title)
            if found_book:
                print(f"Book found: {found_book.book}, Author: {found_book.author}")
            else:
                print("Book not found")

        elif option == 3:
            book_author = input("Type the author: ")
            books_by_author = lib.searchauthors(book_author)
            if books_by_author:
                print(f"Books by {book_author}:")
                for book in books_by_author:
                    print(f"Book: {book.book}, Author: {book.author}")
            else:
                print("Books not found")

        elif option == 4:
            book_title = input("Enter book title to remove: ")
            found_book = lib.searchname(book_title)
            if found_book:
                lib.removebook(found_book)
            else:
                print("Book not found!")

        elif option == 5:
            catalog = lib.librarycatalog()
            if catalog:
                print("Library Catalog:")
                for book in catalog:
                    print(f"Book: {book.book}, Author: {book.author}, Unique ID: {book.uniqueid}")
            else:
                print("The library catalog is empty!")

        elif option == 6:
            print("Have a good day")
            break

        else:
            print("Enter a valid input!")

if __name__ == "__main__":
    main()
#this statement is used to execute the "main()" function when the python is run as the main program