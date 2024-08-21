# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions


# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result = result + arg
    return result


# TODO: pass different arguments
print(addition(20,30))

# TODO: pass an existing list
current_result = addition(1,2,3)
print(current_result)

my_nums = [1, 10, 10, 10]
print ( addition(*my_nums) )
