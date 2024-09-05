# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
# Parentheses is not required
class Book():
    def __init__(self, title):
        self.title = title


# TODO: create instances of the class
# You only need to supply one paramater, whenever you call a method on an object, 
# the object itself gets passed as the 1st argument. Python takes care of that
# self is not the required name , you could use whatever you want
book_one = Book('Brave New World')
book_two = Book("War and Peace")


# TODO: print the class and property
print(book_one)
print(book_one.title)
