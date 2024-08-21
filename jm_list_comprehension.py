# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# TODO: Perform a mapping and filter function on a list
even_squared = list(map(lambda x:x**2, 
                        filter(lambda e:e > 4 and e <16, evens)))
print(even_squared)

even_squee = [x**2 for x in evens if x>4 and x<16]
print(even_squee)

# TODO: Derive a new list of numbers frm a given list

# TODO: Limit the items operated on with a predicate condition
odd_squared = [x**2 for x in odds if x>3 and x<17]
print(odd_squared)