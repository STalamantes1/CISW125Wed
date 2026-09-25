# # signal_color=input("Enter the color of the light")
# # is_blinking=input("Is the light blinking? ")
# # if signal_color=='red':
# #     if is_blinking=="yes":
# #         print("This is a 4 way stop basically")
# #     else:
# #         print("STOP")


# # #Login Program 
# # username=input("What is your username")
# # password=input("What is your password?")
# # if username=='admin':
# #     if password=="cat":
# #         print("Login successful")
# #     else:
# #         print("Password is wrong")
# # else:
# #     print("username is wrong")

# # total_amount = float(input("Enter the total purchase amount: "))
# # is_member = input("Are you a member? (yes/no): ").strip().lower()

# # if total_amount > 200:
# #     discount = 0.15  # 15% discount
# # elif total_amount > 100:
# #     discount = 0.10  # 10% discount
# # else:
# #     discount = 0.0   # No discount

# # if is_member == "yes":
# #     discount += 0.05  # Extra 5% for members

# # final_price = total_amount * (1 - discount)

# # print(f"Total amount: ${total_amount:.2f}")
# # print(f"Applied discount: {discount * 100:.0f}%")
# # print(f"Final price after discount: ${final_price:.2f}")
# if ConvertInput == "DECIMAL":

#     DecimalValue = int(DecimalInput) 
#     DecimalSum = ["0", "0", "0", "0", "0", "0", "0", "0"]

#     while True:
#         if 255 >= DecimalValue >= 128:
#             DecimalSum[0]="1"
#             DecimalValue -= 128
#             print(DecimalValue)
#             print(DecimalSum)
#         elif 128 > DecimalValue >= 64:
#             str.replace(DecimalSum[1], "0", "1")
#             DecimalValue -= 64
#             print(DecimalValue)
#             print(DecimalSum)
#         elif 64 > DecimalValue >= 32:
#             str.replace(DecimalSum[2], "0", "1")
#             DecimalValue -= 32
#             print(DecimalValue)
#             print(DecimalSum)
#         elif 32 > DecimalValue >= 16:
#             str.replace(DecimalSum[3], "0", "1")
#             DecimalValue -= 16
#             print(DecimalValue)
#             print(DecimalSum)
#         elif 16 > DecimalValue >= 8:
#             str.replace(DecimalSum[4], "0", "1")
#             DecimalValue -= 8
#             print(DecimalValue)
#             print(DecimalSum)
#         elif 8 > DecimalValue >= 4:
#             str.replace(DecimalSum[5], "0", "1")
#             DecimalValue -= 4
#             print(DecimalValue)
#             print(DecimalSum)
#         elif 4 > DecimalValue >= 2:
#             str.replace(DecimalSum[6], "0", "1")
#             DecimalValue -= 2
#             print(DecimalValue)
#             print(DecimalSum)
#         elif DecimalValue == 1:
#             str.replace(DecimalSum[7], "0", "1")
#             DecimalValue -= 1
#             print(DecimalValue)
#             print(DecimalSum)
#         else:
#             break

#     print(f"Your decimal value is {"".join(DecimalSum)} in binary!")
#     print("")



username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "password123":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Login failed. Please check your credentials.")


signal_color = input("Enter traffic light color: ")
is_blinking=input("Is the light blinking? ")
if signal_color == "red":
    if is_blinking == 'yes':
        print("Treat this like a 4-way stop.")
    else:
        print("Stop!")
elif signal_color == "yellow":
    if is_blinking == 'yes':
        print("Treat this like a right of way situation. You don't have to stop.")
    else:     
        print("Proceed with caution.")
elif signal_color == "green":
    print("Go!")
else:
    print('Huh?')

signal_color = input("Enter traffic light color: ")
is_blinking=input("Is the light blinking? ")












