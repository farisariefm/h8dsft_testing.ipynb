'''import unit test'''
import unittest

'''importing LibrarySystem and LibraryBook classes from h8dsft_oop module to proceed to create and run unit tests '''
from h8dsft_oop import LibrarySystem, LibraryBook

'''generating a test class, named testLibrarySystem that inherits from unittest.testcase'''
class testLibrarySystem(unittest.TestCase):
    
    '''generating a new function to tests the method of adding a new book into the Library System'''
    def testAddBook(self):
        lib = LibrarySystem ()
        book = LibraryBook ("dilan", "pidi baiq", "1234")
        lib.addbook(book)
        self.assertEqual(len(lib.books),1)
    
    '''generating a new function to tests the method of removing a book from the Library System'''    
    def testRemoveBook(self):
        lib = LibrarySystem()
        book =  LibraryBook ("dilan", "pidi baiq", "1234")
        lib.addbook(book)
        lib.removebook(book)
        self.assertEqual(len(lib.books),0)
    
    '''generating a new function to tests the method of searching books by the title'''    
    def testSearchName(self):
        lib = LibrarySystem()
        book = LibraryBook ("dilan", "pidi baiq", "1234")
        lib.addbook(book)
        found_book = lib.searchname("dilan")
        self.assertIsNotNone(found_book)
        self.assertEqual(found_book.book,"dilan")
        self.assertEqual(len(lib.books),1)
    
    '''generating a new function to tests the method of searching books by the author''' 
    def testSearchAuthor(self):            
        lib = LibrarySystem()
        book = LibraryBook ("dilan", "pidi baiq", "1234")
        lib.addbook(book)
        books_by_author = lib.searchauthors("pidi baiq")
        self.assertNotEqual(len(books_by_author),0)
        for found_book in books_by_author :
            self.assertEqual(found_book.author,"pidi baiq")
        self.assertEqual(len(lib.books),1)
    
        '''generating a new function to tests the method of displaying the catalog of the Library System'''
    def testCatalog(self):
        lib = LibrarySystem()
        book = LibraryBook ("dilan", "pidi baiq", "1234")
        lib.addbook(book)
        catalog = lib.librarycatalog()
        self.assertNotEqual(len(catalog),0)
        for found_book in catalog:
            self.assertEqual(found_book.book,"dilan")
        self.assertEqual(len(lib.books),1)
        
if __name__ == "__main__":
    unittest.main()
    #this statement is used to execute the "unittest.main()" function when the python is run as the main program    
        