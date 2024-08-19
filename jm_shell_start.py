import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # Make a duplicate of an existing file
    # if path.exists("myTextFile.txt"):
    #     # Get the path to the file in the current directory
    #     src = path.realpath("myTextFile.txt") 
    #     print(src)
    #     # Let us make a backup copy by appending ".bak" to the name of the original file
    #     dest = src + ".bak"
    #     shutil.copy(src,dest)
    
    # Rename the original file
    # if path.exists("myTextFile.txt"):
    #     os.rename("myTextFile.txt","renamedTextFile.txt")
        
    # Put things into a zip archive
    # src = path.realpath("myTextFile.txt") 
    # root_dir, tail = path.split(src)
    # shutil.make_archive("my-first-python","zip",root_dir)
    
    # More fine grained zip file
    with ZipFile("test-zip.zip","w") as fine_grained_zip:
        fine_grained_zip.write("myTextFile.txt")
        fine_grained_zip.write("myTextFile.txt.bak")

if __name__ == "__main__":
    main()