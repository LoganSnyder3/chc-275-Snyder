#Problem 1: The hailstone problem (collatz conjecture)

x = input("Enter a number: ")
x = int(x)
while x != 1:
    print(x)
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
        print(x)
print(1)
print("The hailstone sequence has ended.")
    