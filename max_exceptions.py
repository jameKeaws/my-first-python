try:
    number = input("Enter a number: ")
    print(f"Type of number is : {type(number)}")
    result = 2 / number
except Exception as e:
    print(f"Something went wrong, exception is : {e}")