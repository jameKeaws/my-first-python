countries = [
    "Argentina",
    "Australia",
    "Belgium",
    "China",
    "Hong Kong",
    "Thailand",
    "New Zealand"
]

list = [0,1,2,3,4,5,6,7,8,9]

countries_copy = countries.copy()
countries_copy.append("Brazil")

print("\n")
print("After appending Brazil in countries_copy. Below is countries_copy")
print(countries_copy)

print("\n")
print("After appending Brazil in countries_copy. Below is countries")
print(countries)


list_comprehension = [any_x+2 for any_x in list]
print(list_comprehension)
