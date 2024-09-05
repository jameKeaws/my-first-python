# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare Book object to a non Book object")
        if (self.title == other.title 
            and self.author == other.author
            and self.price == other.price):
            return True
        else:
            return False

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare Book object to a non Book object")
        if (self.price >= other.price):
            return True
        else:
            return False

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare Book object to a non Book object")
        if (self.price < other.price):
            return True
        else:
            return False

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
# print(b1 == b3)
# print(b1 == b2)
# print(b1 == "hello")



# TODO: Check for greater and lesser value
# print(b1 >= b2)
# print(b2 < b4)

# TODO: Now we can sort them too
booklist = [b1, b2, b3, b4]
sortedbooklist = booklist.sort()
print([book.title for book in booklist])