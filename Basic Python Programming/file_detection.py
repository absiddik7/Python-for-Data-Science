import os

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists



#file detection
path = "C:\\Users\\Sajib\\Desktop\\Autumn 2021"

if os.path.exists(path):
    print("That location exits")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("That location doesn't exist")

