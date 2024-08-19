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
    Product("Chocopuff", 23, 2, 0.11),
    Product("Whiteout", 24, 3, 0.12),
    Product("Papel", 27, 3, 0.11)
]

# TODO Use the key parameter to select a field to sort on
def product_sort(product):
    return product.price

# print(sorted(product_list, key=product_sort))

# TODO Define an inline lambda function as sorting key
# Inline lambda function > that takes a product object, that uses p.price as the key
print(sorted(product_list, key=lambda p:p.price))

print(sorted(product_list, key=lambda p:p.discount_price()))