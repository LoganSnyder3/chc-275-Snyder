#Problem 2 (mushrooms.py)

small = []
medium = []
large = []

print("Enter mushroom sizes one at a time.")
print("Type 'stop' when you are finished.\n")

check = False
while check == False:
    user_input = input("Enter mushroom size: ").strip().lower()
    if user_input == "stop":
        check = True
    if user_input.isnumeric():
        size = int(user_input)
        if size < 100:
            small.append(size)
        elif size < 200:
            medium.append(size)
        else:
            large.append(size)
    else:
        print(f"'{user_input}' is not a valid number. Please enter a number or type 'stop'.")

print("\nSmall mushrooms:", small)
print("Medium mushrooms:", medium)
print("Large mushrooms:", large)


  
    
    