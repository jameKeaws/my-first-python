import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # # Print the name of the operating system
    # print(f'os.name is {os.name}')
    
    # # Check for item existence and type
    # print("Item exists:", str(path.exists("myTextFile.txt")))
    # print("Item is a file:", path.isfile("myTextFile.txt"))
    # print("Item is a directory:", path.isdir("myTextFile.txt"))
    
    # # Work with file paths
    # print("Item's path:", path.realpath("myTextFile.txt"))
    # my_real_path = path.realpath("myTextFile.txt")
    # print("Item's path and name", path.split(my_real_path))
    
    # Get the modification time
    t = time.ctime(path.getmtime("myTextFile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("myTextFile.txt")))
    
    # Calculate how long ago the item was modified
    time_delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("myTextFile.txt"))
    print("It has been", time_delta, "since the file has been modified")
    print("Or", time_delta.total_seconds(), "seconds")

if __name__ == "__main__":
    main()