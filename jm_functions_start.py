# This is a lesson about basic functions
def function_one():
    print("I am a function_one")
    
def function_two(arg1, arg2):
    print(arg1," ", arg2)
    
def function_cube(x):
    return x * x * x

def power(num, x=1):
    result = 1
    for i in range(x):
        print(f'i is {i}')
        result = result * num
        print(result)

# Allows variable number of arguments
def multi_add(*args):
    # print(arg1)
    result = 0
    for anyItem in args:
        print(f'anyItem {anyItem}')
        result = result + anyItem

# power(4,6)

# power(x=3, num=2)

multi_add(11,22,2,4,11)
    
# function_one()
# function_two("myList",set())

# function_two(10, 10)
# print(function_two(10, 20))

# function_cube(3)
# print(function_cube(3))
