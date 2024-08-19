# TODO Open a file for writing data
# The open function returns a file handle that refers to the file.
# w will overwrite whatever you have in the file
myOwnTextFile = open("myOwnTextFile", "w+")
myOwnTextFile.write("This is me writing on my text file")
myOwnTextFile.close()

# with open("myOwnTextFile", "r") as fp:
#     data = fp.read()
#     print(data)
    

with open("myOwnTextFile", "a+") as file_appender:
    for i in range(10):
        file_appender.write("Hey we are appending \n")
        
    file_appender.seek(0)
    data = file_appender.read()
    print(data)
