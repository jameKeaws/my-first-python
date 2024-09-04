countries = [
    "Canada",
    "Brazil",
    "Australia"         
]
print("Initial contents of countries list")
print(countries)

print("\n")
print("After using countries.insert(0, 'Belgium') ")
countries.insert(0, "Belgium")

print(countries)

countries.remove("Canada")
print("\n")
print("After using countries.remove('Canada') ")
print(countries)

what_was_removed = countries.pop(1)
print("\n")
print(f'what_was_removed : {what_was_removed}')
print("After using countries.pop('1')")
print(countries)

countries.append("Nigeria")
countries.append("Italy")
countries.append("France")
countries.append("Argentina")
print("\n")
print("Before sort list of countries")
print(countries)

print("\n")
print("Sorted list of countries")
countries.sort()
print(countries)

