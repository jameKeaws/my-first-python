# Python Object Oriented Programming by Joe Marini course example
# Checking class types and instances

class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type
print(type(b1))
print(type(b2))
print(type(n1))
print(type(n2))


# TODO: compare two types together
print(type(b1) == type(b2))
print(type(n1) == type(n2))
print(type(n1) == type(b1))


# TODO: use isinstance to compare a specific instance to a known type
print("Checking if b1 and b2 are instance of Book")
print(isinstance(b1, Book))
print(isinstance(b2, Book))
print("Checking if n1 and n2 are instance of Newspaper")
print(isinstance(n1, Newspaper))
print(isinstance(n2, Newspaper))
print("Checking if n1 and b1 are instance of Object, they should be")
print(isinstance(n1, object))
print(isinstance(b1, object))

