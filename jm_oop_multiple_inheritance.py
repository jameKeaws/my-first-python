# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A name"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B name"

# Inherits from A and B
class C(A,B):
    def __init__(self):
        super().__init__()
    
    # Interpreter uses method resolution order
        # Current class > Then super classes as they are defined from left to right
    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)


c = C()
print(C.__mro__)
c.showprops()
