
mystr = "hello"

for char in mystr:
    print(char)
    


print("for i loop")
for i in range(len(mystr)):
    print(mystr[i])

""" 
The same ideas from lists also work for strings
    len() function
    square bracket opertators
    .index()
"""

#Template program
print("1. A")
print("2. B")
print("3. C")
print("4. D")

option = input("Enter your selection: ")
if option == "A":
    print("Executing A")
elif option == "B":
    print("Executing B")
elif option == "C":
    print("Executing C")
elif option == "D":
    print("Executing D")

#This design pattern only works with very strict string parsing.
#String matching had to be as exact as possible

""" 
.strip() - removes leading and trailing whitespace
"""

#Example:
mystr = "       A"
print(mystr)
mystr = mystr.strip()
print(mystr)

option = input("Enter your selection: ")
if option.strip() == "A":
    print("Executing A")
elif option.strip() == "B":
    print("Executing B")
elif option.strip() == "C":
    print("Executing C")
elif option.strip() == "D":
    print("Executing D")

""" 
.lower() - forces everything to be lowercase
.upper() - forces everything to be uppercase
"""

mystr = "A"
print(mystr)
mystr = mystr.lower()
print(mystr)

#Template program 2
print("1. transfer")
print("2. deposit")
print("3. withdraw")
print("4. D")

option = input("Enter your selection: ")
if option.strip().lower() == "transfer":
    print("Executing A")
elif option.strip().lower() == "deposit":
    print("Executing B")
elif option.strip().lower() == "withdraw":
    print("Executing C")
elif option.strip().lower() == "D":
    print("Executing D")
    
""" 
Addition only works if both values are of the same data type
"""

"""
ex = "10" + 5 #This is going to give a type error
              #This is devestating because it crashes the whole program
"""

option = input("Enter a number: ")
option = int(option) #This is how to typecast option into an integer
                     #if you don't input a number into option, you get a value error when trying to typecast
ex = option + 5
print(ex)

"""
isnumeric() - Returns True if the string is called on it's number
"""

option = input("Enter a number: ")
if option.isnumeric():
    option = int(option) 
    
    ex = option + 5
    print(ex)
else:
    print(f"{option} was not a number")
    
    

poem = "asdfqfewqwfa \n asdawdawddwawdaa \n awdawdawfawfwf"
     #\n is called an escape sequence. It stands for "new line"
print(poem)

""" 
.splitlines() - returns a list of strings where each element is split by a newline
"""

lines = poem.splitlines()
print(lines)
