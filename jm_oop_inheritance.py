# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance

class Publication():
    def __init__(self, title, price):
        self.title = title
        self.price = price
        
class Periodicals(Publication):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period
    

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodicals):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


class Newspaper(Periodicals):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

# print(b1.author)
print(f"Book b1 title:{b1.title} author:{b1.author} pages:{b1.pages} price:{b1.price}")
print(f"Newspaper n1 title:{n1.title} period:{n1.period} publisher:{n1.publisher} price:{n1.price}")
print(f"Magazine m1 title:{m1.title} period:{m1.period} publisher:{m1.publisher} price:{m1.price}")
