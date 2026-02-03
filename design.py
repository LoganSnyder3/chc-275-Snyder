def foo():
    print("bar")

def fizz(x):
    if x % 2 == 1: #check if x is even or odd
        print("buzz")
        
def main():
    
    check = True
    while check == True:
        print("Welcome to our test program.")
        print("1. foo")
        print("2. fizz")
        print("type exit to quit")
        option = input("Enter your option: ")
        if option == "1":
            foo()
        if option == "2":
            number = input("What is your number: ")
            try:
                number = int(number)
            except Exception as e:
                print(e)
            else:
                fizz(number)
        if option == "quit":
            check = False
            
if __name__ == "__main__":
    main()