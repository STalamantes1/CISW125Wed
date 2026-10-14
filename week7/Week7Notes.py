# # #What is a loop? 
# # #A loop repeats code 

# # #Repeat this loop 3 times 
# # # for number in range(3):
# # #     #Print Hello each time the loops runs 
# # #     print("hello")


# # #WHILE Loops 
# # #A WHILE loops repeats while a condition is TRUE 

# # #Make a program that is going to print 1-5

# # #Create a variable starting at 1 
# # number=1 #This is our starting point 

# # #Keep looping while number is less than or equal 5
# # # while number<=5: #This is essentially, where will it stop 
# # #     print(number)
# # #     number+=1 #Add 1 to number after each loop 
# # #I want to start counting at 0, count to 50, and get there by increments of 5 
# # # number2=0
# # # while number2<=50:
# # #     print(number2)
# # #     number2+=5


# # #A while loop is useful when you want to keep asking until the user gives a valid answer 
# # #Ask the user for their age 
# # # age=int(input("Enter your age: "))

# # # #Keep looping if the age is less than 1 or greater than 120 
# # # while age < 1 or age >120: #The loop only runs is one of the conditions is true 
# # #     #Tell the user, invalid input
# # #     print("Invalid Age ")

# # #     #ask the user to enter their age again
# # #     age=int(input("Enter your age: "))
# # # #This runs after the loop finishes 
# # # print("Thank you ")


# # #FOR LOOP 
# # #A FOR loop works through items one at a time 

# # #Create a list containing 3 games 
# # # games=["Minecraft","Mario", "Zelda"]
# # # cars=["Honda", "Acura", "BMW"]
# # # #Take one item from the games list at a time
# # # for game in games:
# # #     #Print the current game
# # #     print(game)
# # # #Each time the loop repeats, game holds the next item in the list 
# # # for i in cars:
# # #     print(i)

# # #Range
# # #Range() creates a sequence of numbers
# # # #Starts at 2 and stops right before 8 
# # # for number in range(2,8): 
# # #     #(starting number, stop right before this number)
# # #     #Print the current number
# # #     print(number)
# #     #Remember: The ending number in range() is not included

# # #We can also perform calculations inside the loop:
# # # #Loop through numbers 2 through 7 
# # # for number in range(2,8):
# # #     #multiply the number by itself
# # #     square=number*number
# # #     #print the squared number
# # #     print(square)


# # #Looping through a string 
# # #Store a name inside the string 
# # name="Sebastian"
# # #Take one character from the string at a time 
# # for letter in name:
# #     print(letter)
# # #This works very similar to how we loop through a list 


# # #USING BREAK
# # #BREAK stops a loop early 

# # #Loop through numbers 1-10
# # # for number in range(1,11):
# # #     #print the current number
# # #     print(number)
# # #     #Break the loop when number hits 5
# # #     if number==5: #Everything after the : runs only if the condition is true 
# # #         #once number is equal to 5, loop will stop (Break)
# # #         break


# # #Nested LOOP 
# # #Nested loop is a loop inside another loop 

# # #Outer loop run through 1,2,3
# # # for number in range(1,4):
# # #     #inner loop also runs through 1,2,3
# # #     for number2 in range(1,4):
# # #         print(number,number2)

# # #CHOOSING the right loop?
# # #Use a while loop when repetition depends on a condition 

# # #Keep looping while answer is not yes 
# # while answer !="yes":
# #     #ask the user again
# #     answer=input("Enter yes: ")

# # #Use a for loop when working through items
# # #Go through each item in the list 
# # items=["apples","Oranges","Kiwis"]
# # for item in items:
# #     #print the current item
# #     print(item)

# # #Use FOR with RANGE() when working through numbers 

# # #Loop through 1-10
# # for number in range(1,11):
# #     #Print the current number
# #     print(number)

    

# # Countdown Timer
# seconds=int(input('Enter the time you want to countdown from: '))
# while seconds>=0:
#     if seconds==3:
#         print("Almost There")
#     elif seconds==0:
#         print("Times up")
#     else:
#         print(seconds)
#     seconds-=1


# #Bank Program 
# # balance=1000
# # while True:
# #     print(f"{balance}, Balance")
# #     choice=input("Deposit, withdraw or exit").lower()
# #     if choice=="deposit":
# #         amount=float(input("Amount: "))
# #         balance+=amount
# #     elif choice=="withdraw":
# #         amount=float(input("How much money you want to take out "))
# #         if amount>balance:
# #             print("Not enough funds")
# #         else:
# #             balance-=amount
# #     elif choice=="exit":
# #         break 
# # print(f"Final balance: {balance}")


# #Random number generator 
# # print("Guess the number: ")
# # target=4
# # while True: 
# #     guess=int(input("Enter your guess"))
# #     if guess<target:
# #         print("too low")
# #     elif guess>target:
# #         print("Too high ")
# #     else:
# #         break #correct guess exit loops 
# # print("Correct!")


# #Create a grocery list 
# #make an empty list 
# list=[]
# while True:
#     #Ask the user if they want to add an item to the list 
#     userInput=input("Do you want to add to the list? ").lower()
#     if userInput=="yes":
#         item=input("Enter the item to add")
#         list.append(item)
#     elif userInput=="no":
#         break
#     else:
#         print("Invalid input")
        
target=4 #This is the number the user has to guess 
max_guesses=3
guesses_used=0 
won=False #This will change if the user guesses correctly 

while guesses_used<max_guesses:
    guess=int(input("Enter your guess (1-7): "))
    guesses_used+=1

    if guess<target:
        print("Too Low")
    elif guess>target:
        print("Too High")  
    else:
        won=True
        break
#After the loop ends, win/lose message 
if won:
    print("You win!")
else:
    print("Ran out of guesses")
    print(f"The was {target}")


# list=[]
# while True:
#     item=input("Do you want to add items to your list (yes or no)").lower()
#     if item=="yes":
#         list_item=input("What do you want to add? ")
#         list.append(list_item)
#         print("Item Added!")
#     elif item == "no":
#         break
#     else:
#         print("Invalid response, yes or no only")
    
#     print("\n YOur list is")
#  for i in list:
#         print(f"- {list_item}")
    
grocery_list = []  # Start with an empty list

while True:
    choice = input("Would you like to add something to the list? (yes/no): ").lower()

    if choice == "yes":
        item = input("What item would you like to add? ")
        grocery_list.append(item)
        print("Item added!\n")
    elif choice == "no":
        break  # exit the loop
    else:
        print("Please type yes or no.\n")

print("\nYour grocery list:")

# Neat way: loop through each item
for item in grocery_list:
    print(f"- {item}")

# (If the list is empty, this will just print the header and nothing else.)
