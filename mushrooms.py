#Problem 2 (mushrooms.py)

mushrooms = []
check = False
while check == False:
    print("Welcome to the mushroom program")
    print("1. Enter the size of your mushroom")
    print("2. Sort mushrooms into groups")
    print("3. quit")
    option = input("Enter your option: ")
    if option == "1":
        option = input("Enter the size of your mushroom: ")
        if option.isnumeric():
            option = int(option)
            if option >= 100:          
        else:
            print(f"{option} was not a number")        
    elif option == "2":
        
    elif option == "3":
       print("Goodbye")
       check = True
    else:
        print("Not a valid option")
  
    
    