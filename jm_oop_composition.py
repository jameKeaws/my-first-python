# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)
        
    def getbookpagecount(self):
        result = 0
        for any_chapter in self.chapters:
            result = result + any_chapter.pagecount
        return result

class Author():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Chapter():
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

b1_author = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, b1_author)

chapter_1 = Chapter("Chapter 1", 125)
chapter_2 = Chapter("Chapter 2", 97)
chapter_3 = Chapter("Chapter 3", 143)

b1.addchapter(chapter_1)
b1.addchapter(chapter_2)
b1.addchapter(chapter_3)

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())
