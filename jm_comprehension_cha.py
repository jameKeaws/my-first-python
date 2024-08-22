import string

show_expected_result = False
show_hints = False

l = 0
num_chars = 0
num_punct = 0
num_unique = 0
unique_str = ""

def calc_values(the_str):
    global l, num_chars, num_punct, num_unique, unique_str
    print(the_str)
    # YOUR CODE GOES HERE
    # Just set the values of the global variables,
    # there is no need to return a value from this function
    l = len(the_str)
    num_chars = len([anyC for anyC in the_str if anyC in string.digits])
    num_punct = len([anyC for anyC in the_str if anyC in string.punctuation])
    num_unique = len({anyC for anyC in the_str if anyC in string.ascii_letters})
    unique_set = {anyC for anyC in the_str if anyC in string.ascii_letters}
    print(unique_set)
    unique_str = ''.join(str(anyC) for anyC in unique_set if anyC in string.ascii_letters)