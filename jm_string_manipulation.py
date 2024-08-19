test_string_1 = "The quick brown fox jumps over the lazy dog on the 1st of December"

# TODO upper and lower convert between cases
print(test_string_1.upper())
print(test_string_1.lower())

# TODO Use the split and join functions
split_str = test_string_1.split(" ")
print(split_str)

letters = ["the", " ", "a", "b", "e", "l"]
print(", ".join(letters))

# TODO Use justification functions to align strings
# ljust, center, rjust
names = ["Amy", "Susan", "Fred", "Yan Choon", "Holly", "Noah", "Matt"]
biggest = max (len(name) for name in names)
print(biggest)

for name in names:
    print(name.ljust(biggest+2,"-") + ":")
    
for name in names:
    print(name.rjust(biggest+2,"-") + ":")

for name in names:
    print(name.center(biggest+2,"-") + ":")
    
# TODO Use a translation table to replace characters
sampleStr = "The quick brown fox jumps over the lazy dog"

trans_table = str.maketrans("abegilostz","4636110572")
print(sampleStr)
print(sampleStr.translate(trans_table))
