# print("Hello", "there", "world")
# print(bin(8))
# print(oct(64))
# print(hex(32))
# print(int('1010',2))

# name = "Max"
# print(name)

# mart = '''
# This is a multi line
# quoted string
# '''
# print(mart)

# quoted_string = "Father's day"
# print(quoted_string)

# name = "Maximiliano's courses"
# message = name + " " + "are great"
# print(message)
# print(message.lower())
# print(message.upper())
# print(message.title())

# message = "  Pethon "
# print(message.strip())

# new_message = message.replace("Max", "Car")
# print(new_message)
# # Count how many times a string appears
# print(new_message.count("e"))
# # Find index
# print(new_message.find("Car"))

# for x in range(6):
#     print(x)
    
# for number in range(4, 0, -1):
#     print(number)

total = 0
while input("Enter more stock, Y/n: ")=='Y':
    stock_quantity = int(input("Enter stock quantity: "))
    if stock_quantity < 0:
        break
    print(f"We are going to add stock_quantity : {stock_quantity} to the total : {total}")
    total +=stock_quantity
    print(f"Making the total : {total}")
# The else condition will not be triggered if the while condition hits the break
else:
    print(f"Total is {total}")
