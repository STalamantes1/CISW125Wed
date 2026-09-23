signal_color=input("Enter the color of the light")
is_blinking=input("Is the light blinking? ")
if signal_color=='red':
    if is_blinking=="yes":
        print("This is a 4 way stop basically")
    else:
        print("STOP")


#Login Program 
username=input("What is your username")
password=input("What is your password?")
if username=='admin':
    if password=="cat":
        print("Login successful")
    else:
        print("Password is wrong")
else:
    print("username is wrong")

total_amount = float(input("Enter the total purchase amount: "))
is_member = input("Are you a member? (yes/no): ").strip().lower()

if total_amount > 200:
    discount = 0.15  # 15% discount
elif total_amount > 100:
    discount = 0.10  # 10% discount
else:
    discount = 0.0   # No discount

if is_member == "yes":
    discount += 0.05  # Extra 5% for members

final_price = total_amount * (1 - discount)

print(f"Total amount: ${total_amount:.2f}")
print(f"Applied discount: {discount * 100:.0f}%")
print(f"Final price after discount: ${final_price:.2f}")
