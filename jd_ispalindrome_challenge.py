import string
import re

mytext = input("Enter string to evaluate:")
# Reference : https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
# https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
mytext = re.sub('[^A-Za-z0-9]+', '', mytext).lower()
print(mytext)

forwardlist = list(mytext)
print(forwardlist)
reversedlist = list(mytext[::-1])
print(reversedlist)

listlength = len(forwardlist)
print("The length of list : ", listlength)

# Loop over the list
i = 0
is_palindrome = True
while i < listlength:
    if(forwardlist[i] != reversedlist[i]):
        is_palindrome = False
        break
    i+=1
    
if is_palindrome:
    print(f"mytext {mytext} is a palindrome")
else:
    print(f"mytext {mytext} is not a palindrome")

