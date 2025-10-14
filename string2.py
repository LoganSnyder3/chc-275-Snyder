mystr = "Frank Teague Preston"  #All of my names are in one string but seperated by spaces

""" 
I can split mystr into a list of individual strings by using .split()
"""

names = mystr.split()   #This will split the string into a list of elements where each element is seperated by the whitespaces
print(names)

mystr = "11010101Hello11010101World11010101How11010101Are11010101You11010101"

msg = mystr.split("11010101")
print(msg)

""" 
.join() - you can think of this as being the inverse of .split()
"""

space = " " #You wouldn't typically create a variable for black spaces.
newmsg = space.join(msg)
print(newmsg)


newmsg = " ".join(msg).strip() #You can chain fuctions together
print(newmsg)

#Template program
print("1. transfer")
print("2. deposit")
print("3. withdraw")
print("4. D")

option = input("Enter your selection: ").strip().lower()
if option == "transfer":
    print("Executing A")
elif option == "deposit":
    print("Executing B")
elif option == "withdraw":
    print("Executing C")
elif option == "D":
    print("Executing D")

"""
-lower()
-upper()
-strip()
-isnumeric()
-split()
-splitlines()
-join()
"""

#You can add numbers together just using the plus sign

sum = 5 + 4 #completely valid

str1 = "Hello"
str2 = "World"
joined = str1 + str2    #This concatenates str1 to str2
joined2 = str2 + str1
print(joined)
print(joined2)