countries = (
    "Argentina",
    "Australia",
    "Belgium",
    "China",
    "Hong Kong",
    "Thailand",
    "New Zealand"
)
print("Initial content of countries as tuples")
print(countries)

print(countries[:2:])

# If there is no trailing comma after a single element inside a parentheses, then it will be type str instead of type tuple.
not_a_tuple = ("Brazil")
print(type(not_a_tuple))

print("\n")
print("Forced tuple of 1 element")
forced_tuple = ("Brazil",)
print(type(forced_tuple))

tup_1 = (1,) + (1,) + (1,)
print(tup_1)

# The id() function returns a unique id for the specified object.
# All objects in Python has its own unique id.
# The id is assigned to the object when it is created.
# The id is the object's memory address, and will be different for each time you run the program. (except for some object that has a constant unique id, like integers from -5 to 256)
data = {'name': 'Peter', 'age': 22}
another_data = data.copy()
print(f'id(data) is {id(data)}')
print(f'id(another_data) which was created via data.copy() is {id(another_data)}')

same_data = data
print(f"id(same_data) is {id(same_data)}")
