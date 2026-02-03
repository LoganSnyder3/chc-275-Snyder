def makelist():
    numbers = []
    while True:
        user_input = input("Enter a number or type stop to finish: ")
        if user_input.lower() == "stop":
            break
        if user_input.isnumeric():
            numbers.append(int(user_input))
        else:
            print("Please enter a valid integer.")

    return numbers

list1 = makelist()
print(list1)

list2 = makelist()
print(list2)