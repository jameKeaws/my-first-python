# the key parameter can be used to sort complex objects
from operator import attrgetter, methodcaller, itemgetter

class Product():
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount
    
    def __repr__(self):
        return repr((self.name, self.price, self.weight))
    
    def discount_price(self):
        # print(self.name)
        # print(self.price - (self.price * self.discount))
        return self.price - (self.price * self.discount)
    
    
product_list = [
    Product("Widget A", 50, 10, 0.05),
    Product("Widget B", 40, 8, 0.15),
    Product("Widget C", 35, 12, 0.0),
    Product("Widget D", 65, 7, 0.20),
    Product("Widget E", 70, 7, 0.12)
]

# TODO The operator module functions provide easy ways to select fields
# attrgetter() retrieves a given attribute or property from an object
# itemgetter() retrieves an item at a given index in a collection
# methodcaller() calls the given method on the object
print("Using the attrgetter() method:")
print(sorted(product_list, key=attrgetter("weight"), reverse=True))

# Using methodcaller to invoke a method
print("Using the methodcaller() method:")
print(sorted(product_list, key=methodcaller("discount_price")))

# Use the itemgetter to retrieve an index
inventory =[("Widget A", 5), ("Widget B", 2), ("Widget C", 4), ("Widget D", 7), ("Widget E", 4)]
print(sorted(inventory, key=itemgetter(1), reverse=True))