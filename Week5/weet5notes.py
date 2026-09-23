#BMI Checker
height=float(input("Enter your height (inches): "))
weight=float(input("Enter your weight (pounds): "))

height2=height*height
BMI=(weight/height2*703)
print (BMI) 
if BMI<18.5:
    print("You are underweight.")
elif BMI==18.5 or BMI<=24.9:
    print("You are healthy.")
elif BMI==25 or BMI<=29.9:
    print("You are overweight.")
else:
    print("You are obese")
