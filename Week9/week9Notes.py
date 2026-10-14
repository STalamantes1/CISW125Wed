#Learn how to write, read and edit files using python 
#Common modes when using Files 

# "r"=read only 
#You can read this file, but cant change it 
#Error if file doesnt exist 

#"w"= write
#Create the file if it doesnt exist 
#Overwrites the file if it does exist (Deletes old content)

#"a"=append
#Creates the file if it doesn't exit 
#Adds new text to the file, does not delete existing content 

#with open("FolderName/filename","mode")
# with open("Week9/stuff.txt","r") as file:
#     contents=file.read()
#     print(contents)

#I want to completely overwrite the content in stuff.txt
# with open("Week9/stuff.txt","w") as file:
#     file.write("THis line appears underneath")
#Once we leave the identation block, the file is automatically closed 

#Reading from a file 
#Mehtod A: Read the whole file at once 
# with open("Week9/stuff.txt","r") as file:
#     contents=file.read()
#     print(contents)


#Method B: Read line by line using a for loop 
# with open("Week9/stuff.txt","r") as file:
#     for line in file:
#         print(line)


# Appending to a file (Adding to a file)
# Appending adds to the end of a file without deleting what's already there
# with open("Week9/stuff.txt","a") as file:
#     file.write("\n")
#     file.write("This should appear at the very end, cause we used mode A")
# # We use R mode to verify if a file exists 

# with open("Week9/newFile","a") as file:
#     file.write("\n Cat")


name=input("What is your name: ")
age=input("What is your age? ")
