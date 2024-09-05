# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random


@dataclass
class Book:
    def price_func():
        return float(random.randrange(20, 40))
    
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)
    
b1 = Book()
print(b1)

b2 = Book("War and Fish", "Leo Tolstory", 265)
b3 = Book("Cather in the Rye", "JD Salinger", 350)
print(b2)
print(b3)
