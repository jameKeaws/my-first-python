import string

sampleStr = "The quick brown fox jumps over the lazy dog over"

# TODO startsWith and endsWith function
print(sampleStr.startswith("The q"))
print(sampleStr.startswith("the"))
print(sampleStr.endswith("dog"))
print(sampleStr.endswith(" dog"))

# TODO The find and rfind functions
print(sampleStr.find("fox"))
print(sampleStr.rfind("fox"))

# TODO in function
print("brown fox" in sampleStr)

# TODO replace function
newStr = sampleStr.replace("brown", "green")
print(newStr)

# TODO counting instances of substring
print(sampleStr.count("over"))