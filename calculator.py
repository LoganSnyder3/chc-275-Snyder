check = False
while check == False:
    print("Welcome to my 4-function calculator")
    print("Which function to execute?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    option = input("Enter which function to execute: ")
    if option.strip() == "1":
        try:
            x = int(input("Enter Num 1: "))
            y = int(input("Enter Num 2: "))
            sum = x + y
            print(sum)
        except ValueError: 
            print("x and y must be numbers")
        except TypeError:
            print("x and y must be integers")
        except Exception as e:
            print(e)
        finally:
            print("Thanks for using my calculator")
    elif option.strip() == "2":
        try:
            x = int(input("Enter Num 1: "))
            y = int(input("Enter Num 2: "))
            difference = x - y
            print(difference)
        except ValueError: 
            print("x and y must be numbers")
        except TypeError:
            print("x and y must be integers")
        except Exception as e:
            print(e)
        finally:
            print("Thanks for using my calculator")
    elif option.strip() == "3":
        try:
            x = int(input("Enter Num 1: "))
            y = int(input("Enter Num 2: "))
            product = x * y
            print(product)
        except ValueError: 
            print("x and y must be numbers")
        except TypeError:
            print("x and y must be integers")
        except Exception as e:
            print(e)
        finally:
            print("Thanks for using my calculator")
    elif option.strip() =="4":
        try:
            x = int(input("Enter Num 1: "))
            y = int(input("Enter Num 2: "))
            quotient = x / y
            print(quotient)
        except ValueError: 
            print("x and y must be numbers")
        except ZeroDivisionError:
            print("y must be nonzero")
        except TypeError:
            print("x and y must be integers")
        except Exception as e:
            print(e)
        finally:
            print("Thanks for using my calculator")
    elif option.strip() == "5":
        print("Goodbye")
        check = True
    else:
        print("Invalid option")

    
    


