#Problem 3: powerlevels.py
num1 = input("Enter Number 1: ")
num1 = int(num1)
num2 = input("Enter Number 2: ")
num2 = int(num2)
if num1 > num2: 
    print("Number 1 wins")
elif num1 < num2:
    print("Number 2 Wins")
elif num1 == num2:
    print("Its a Tie")

