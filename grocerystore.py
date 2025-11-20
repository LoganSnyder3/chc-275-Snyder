#Lab 4 - Grocery Store

#Menu
print("Welcome to the grocery store")
print("1. Add to cart")
print("2. Remove items")
print("3. Check out")
option = input("Enter your selection: ")


if option == "1":
    try:
        file = open("foods.txt", "r")
        buffer = file.readlines()
        foods = []
        prices = []
        print(buffer)
    except FileNotFoundError:
        print("foods.txt not found.")
        foods = []
        prices = []
    except Exception as e:
        print("Error reading foods.txt:", e)
        foods = []
        prices = []
    else:
        file.close()