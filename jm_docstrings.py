# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions
import collections

# print(str.__doc__)
# print(collections.__doc__)

def my_function(arg1, arg2=None):
    """_summary_

    Args:
        arg1 (_type_): _description_
        arg2 (_type_, optional): _description_. Defaults to None.
    """
    print(arg1, arg2)


print(my_function.__doc__)
