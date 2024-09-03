myInt = 5
myStr = 'This is a global string'
myList = [1,2,'three',False,4]
myDictionary = {"a":"apple" , "b":"benene"}
myTuple = ("a","b","c")
mySet = set()

print(myInt)
print(myList)
print(myDictionary)
print(myTuple)

myInt = "five"
print(myInt)

print(myList[2])
print(myList[0:5:2])
print(myList[::-1])
print(myDictionary["a"])
print("string type" + str(123))


def someFunction():
    # Using the global variable
    # global myStr
    myStr = "myStr value inside someFunction"
    print(f'This is inside the function : {myStr}')
    
    
someFunction()
print(f'This is outside the function : {myStr}')

del(myStr)
print(myStr)