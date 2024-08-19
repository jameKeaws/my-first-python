from array import array

# TODO Create an array of integer numbers

arr_1 = array('i',[2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
print(arr_1.typecode)
print("Array 1 item size", arr_1.itemsize)

# TODO Add additional items to the array
arr_1.insert(0, 0)
arr_1.append(22)
arr_1.extend([24, 26, 28, 30])
print(arr_1)

# TODO Iterate over the array content like any other list
for i,item in enumerate(arr_1):
    print(f'i: {i}')
    print(f"item: {item}")
    
# TODO Try to add a non integer number into the array
# arr_1.append(20.5)

# TODO Create an array to hold bytes instead of integers.  Bytes are from 0 to 255
arr_2 = array('B', [8, 16, 32, 64, 128, 255])
print(arr_2.typecode)
print(arr_2.itemsize)

# TODO Try to add an item that is out of range e.g. 256
arr_2.append(20)
# arr_2.append(256)

# TODO Convert an efficient array to a list
list_1 = arr_1.tolist()
print(arr_1)
print(list_1)