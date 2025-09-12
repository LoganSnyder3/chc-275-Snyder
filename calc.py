""" 
Make a four function calculator that takes in two numbers PER operation

1) Take in two numbers
2) Add the together
3) print the sum

1) Take in two numbers (use input to save the sumbers into variables)
2) Subtract them
3) Print the difference

Do this for all four math functions that we have

Use f-strings, variables, input() and typecasting
"""

num1 = input("Enter num 1: ")
num2 = input("Enter num 2: ")
num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

num3 = input("Enter num 3: ")
num4 = input("Enter num 4: ")
num3 = int(num3)
num4 = int(num4)
difference = num3 - num4
print(f"The difference of {num3} and {num4} is {difference}")

num5= input("Enter num 5: ")
num6 = input("Enter num 6: ")
num5 = int(num5)
num623 = int(num6)
product = num5 * num6
print(f"The product of {num5} and {num6} is {product}")

num7= input("Enter num 7: ")
num8 = input("Enter num 8: ")
num7 = int(num7)
num8 = int(num8)
quotient = num7 / num8
print(f"The quotient of {num7} and {num8} is {quotient}")
