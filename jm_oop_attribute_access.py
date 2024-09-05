# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, attr_name):
        # Note : As we are in the function that is being called when an attribute is being accessed 
        # we could not access an attribute in here, as it will create an infinite loop 
        if attr_name == "price":
            # We need to call the super().__getattribute__() version
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        # And if we are not operating on price attribute, we need to just call the super().__getattribute__(attr_name)
        return super().__getattribute__(attr_name)
            
            

    # TODO: __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attribute must be a float")
        return super().__setattr__(name, value)

    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
        # __getattr__ only gets called if the __getattribute__ method version is not defined
        # OR if it throws an exception
        # OR if the attribute does not exist
    def __getattr__(self, attr_name):
        return f"{attr_name} is not here"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

b1.price = 40.0
print(b1.randomproperty)

