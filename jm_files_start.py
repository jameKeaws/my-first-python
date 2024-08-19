def main():
    # print('file_start_jm.py')
    # Open a file for writing.  Create the file, if the file does not exist yet
    # myTextFile = open("myTextFile.txt","w+")
    
    # Update an existing file
    # myTextFile = open("myTextFile.txt","a+")
    
    # Write some lines of data into the file
    # for x in range(10):
    #     myTextFile.write("This is updated text in the file \n")
    
    # Open the file for reading. No need to close the file when reading it
    myTextFile = open("myTextFile.txt","r")
    if myTextFile.mode == 'r':
        # contents = myTextFile.read()
        # print(contents)
        
        file_lines = myTextFile.readlines()
        for any_line in file_lines:
            print(any_line)
        
    # When we are done close the file
    # myTextFile.close()

if __name__ == "__main__":
    main()