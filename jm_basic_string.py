import string

# TODO Predefined string constants can be used in certain scenarios
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(string.hexdigits)

# TODO Use the constants to filter information out
test_string_1 = "The quick brown fox jumps over the lazy dog on the 1st of December"
test_string_2 = "Supercalifragilistic"
test_string_3 = "90210"

# TODO String testing methods
result = "".join([any_char for any_char in test_string_1 if any_char in string.ascii_letters])
print(result)

print(test_string_1)
print(test_string_1.isalnum())
print(test_string_2)
print(test_string_2.isalnum())

print(all([anyChar.isalpha() for anyChar in test_string_1]))
print(test_string_1.isnumeric())
print(test_string_3.isnumeric())
