#Lab 4 - Grocery Store

#Menu
print("Welcome to the grocery store")
foods = []
prices = []

try:
    file = open("foods.txt", "r")
    buffer = file.readlines()
    file.close()

    for i in range(len(buffer)):
        line = buffer[i].strip()
        parts = line.split(",")

        foods.append(parts[0])
        prices.append(parts[1])

    print(foods)
    print(prices)
    
except:
    print("foods.txt not found.")

cart = []
quantities = []

check = False
while check == False:
    print("1. Add to cart")
    print("2. Remove items")
    print("3. Check out")
    option = input("Enter your selection: ")

    if option == "1":
        print("Select an item to add:")
        for i in range(len(foods)):
            print(i, foods[i], prices[i])
        
        item = int(input("Enter item number: "))
        quantity = int(input("Enter quantity: "))

        cart.append(item)
        quantities.append(quantity)

        print("Item added to cart.")

    elif option == "2":
        if len(cart) == 0:
            print("Cart empty.")
        else:
            print("Items in cart:")
            for i in range(len(cart)):
                print(i, foods[cart[i]], quantities[i])
            
            index = int(input("Enter cart index to remove: "))
            cart.pop(index)
            quantities.pop(index)
            print("Removed.")

    elif option == "3":
        sum_money = 0

        for i in range(len(cart)):
            index1 = cart[i]
            quantity = quantities[i]

            price1 = prices[index1]
            parts = price1.split(".")
            cents = int(parts[0]) * 100 + int(parts[1])

            sum_money = sum_money + (cents * quantity)
        
        tax = sum_money * 6 // 100
        total = sum_money + tax

        print(f"Subtotal: ${sum_money/100:.2f}")
        print(f"Tax: ${tax/100:.2f}")
        print(f"Total: ${total/100:.2f}")
        check = True

    else:
        print("Invalid choice.")
