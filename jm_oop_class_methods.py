# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK","EBOOK")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    
    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    # This does not take arguments
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
            
    

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle
        
    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print(f"Book types : {Book.get_book_types()}")


# TODO: Create some book instances
book_1 = Book("Undercover", "HARDCOVER")
book_2 = Book("Underdark", "EBOOK")


# TODO: Use the static method to access a singleton object
the_books = Book.getbooklist()
print(the_books)
the_books.append(book_1)
print(the_books)
the_books.append(book_2)
print(the_books)