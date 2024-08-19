class Product():
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount
    
    def __repr__(self):
        return repr((self.name, self.price, self.weight))
    
    def discount_price(self):
        print(self.name)
        print(self.price - (self.price * self.discount))
        return self.price - (self.price * self.discount)
    
    
product_list = [
    Product("Mallows", 35, 1, 0.10),
    Product("Chocopuff", 23, 10, 0.11),
    Product("Whiteout", 24, 3, 0.12),
    Product("Papel", 27, 3, 0.11),
    Product("Chocopuff", 23, 7, 0.11)
]
# print(sorted(product_list, key=lambda p:p.price))

initial_sort_list = sorted(product_list, key=lambda p:p.weight)
print(initial_sort_list)
print(sorted(initial_sort_list, key=lambda p:p.price, reverse=True))