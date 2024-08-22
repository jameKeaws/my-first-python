# Python code​​​​​​‌​‌‌‌​​‌‌‌​‌​​​​​‌‌‌​‌‌‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

class Book():
    def __init__(self, title, author, pages, cover, antique, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.cover = cover
        self.antique = antique
        self.price = price

    # TODO: Implement the str and repr functions
    def __str__(self):
        return f"{self.title} by {self.author}: {self.pages}, {self.cover}, {self.price}"

    def __repr__(self):
        return f"<Book:{self.title}:{self.author}:{self.pages}:{self.cover}:{self.antique}:{self.price}>"


    def __getattr__(self, attr):
        # If requested attributed is adjustedprice
        if attr == "adjustedprice":
            adjusted_price = self.price
            if self.cover == "Paperback":
                adjusted_price = self.price = self.price - 2
            if self.antique == True:
                adjusted_price =  self.price = self.price + 10
            return adjusted_price
        if attr == "genre":
            return ""
        else:
            raise AttributeError(f"attr {attr} requested is not valid")


    # TODO: Implement comparisons <, >, <=, >=
    def __gt__(self, other):
        return self.pages > other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __ge__(self, other):
        return self.pages >= other.pages

    def __le__(self, other):
        return self.pages <= other.pages