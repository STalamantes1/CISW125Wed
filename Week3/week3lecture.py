# #Whats the difference between int and float? 
# #Int is whole numbers, no decimal point (10,2,5,6,7,)
# #Float contains decimals(10.25,12.058,12.52)


# x=15 #int value 

# y=2 #float

# print(x,type(x))
# print(y,type(y))

# print(x//y) #// floor division, will give whole number value 
# print(x/y) #/ regular division, this will give float(decimal) value

# user_text=input("Type something: ")
# print(f"Hello, {user_text}")


#user input automatically converts input to string, 
# regardless of what we have typed
# age_text=input("What is your age?: ") #asks for age, makes input string
# age_int=int(age_text) #converting variable on line 22 into an INT 
# print(age_int, type(age_int))

#string is text data 
# message = "CISW 125"
# print(message, type(message))

# word="Python"
# print(word[0])#This selects the first character of my word
# print(word[1])#This selects the second character
# print(word[2])#This selects the third character of my word
# print(word[3])#This selects the fourth character3
# print(word[5])#This selects the fifth character of my word

# #Slicing is when we want to print a range from string text 
# print(word[0:3])
#start:end means start at and stop before end [start:end]

#Built in python functions, 
#.upper(), this covnerts string to all UPPER CASE
#.lower(), this converts string to all LOWER CASE
# phrase="Hello, world"
# print(phrase.upper())
# print(phrase.lower())


fruits=["apple","banana","oranges"]
numbers=[10,2,3.5]
mixed=[100,"score",3.5]

print(fruits[0]) #This prints my first item in my list 
print(fruits[0:2]) #This prints my first 2 items 
#to add to a list, we append the list name
fruits.append("Kiwi")
print(fruits)



