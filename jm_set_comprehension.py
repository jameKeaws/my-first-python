# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use set comprehensions


# define a list of temperature data points
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

# TODO: build a set of unique Fahrenheit temperatures
ftemps1 = [(t * 9/5) + 32 for t in ctemps]
print(ftemps1)

ftemps_list = [(t * 9/5) + 32 for t in ctemps]
ftemps_set = set((t * 9/5) + 32 for t in ctemps)
ftemps_cleaner = {(t * 9/5) + 32 for t in ctemps}
print(ftemps_list)
print(ftemps_set)
print(ftemps_cleaner)

# TODO: build a set from an input source
s_temp = "The quick brown fox jumped over the lazy dog"
char_set = {c.upper() for c in s_temp if not c.isspace()}
print(char_set)

