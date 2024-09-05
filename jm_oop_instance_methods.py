# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price, edition):
        self.title = title
        # TODO : add instance properties
        self.author = author
        self.pages = pages
        self.price = price
        self.edition = edition
        # _ indicate that attribute or method is intended only to be used by the class
        # __ then the Python interpreter will change the name of the property if other classes try to access it
        self.__secret = "This is a secret attribute"

    # TODO: create instance methods
    def get_price(self):
        # If an attribute is not defined in __init__, we can't rely on it being present
        # We need to test for it's presence first, before using it
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def set_discount(self, amount):
        # The _ in front of the attribute gives other developers 
        # a hint that this attribute is internal to the class
        self._discount = amount

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95, "3rd")
b2 = Book("The Catcher in the Rye", "JD Salinger", 1000, 50.00, "4th")
b2.set_discount(.10)
# TODO: print the price of book1
# print(f'Price of book 1 without a discount : {b1.get_price()}')
# print(f'Price of book 2 with set discount of 10% : {b2.get_price()}')

# TODO: try setting the discount


# TODO: properties with double underscores are hidden by the interpreter
# print(b1._Book__secret)
print(b1.__secret)