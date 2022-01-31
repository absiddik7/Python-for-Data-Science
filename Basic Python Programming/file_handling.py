import shutil
import os

#write file
text = "hello \nThis text is from write file\n"
text2 = "Hi \nThis text is from append file"
try:
    with open('testFile.txt','w') as file: # the existing file content will be overwrite
        file.write(text)

    with open('testFile.txt','a') as file: # new text will append with existing file content
         file.write(text2)

    #read file
    with open('testFile.txt','r') as file: # with will automaticly close the file after read and its a good practice
        print (file.read())
    
    path = "C:\\Users\\Sajib\\Desktop\\test.txt" # file path from pc
    with open(path,'r') as file: # we can do read, write, delete on pc file 
        print(file.read())

    src = 'testFile.txt'
    dst = 'copy.txt'
    shutil.copyfile(src, dst) # src, dst (destination). this will create copy.txt file in prject folder and past the content to it

except FileNotFoundError as e:
    print(e)

#delete file
try:
    os.remove('newFile.txt')
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You do not have permission to delete the file")
except Exception:
    print("Something wrong!")



