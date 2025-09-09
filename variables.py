x=5
print(x)

y=10
print(x + y)
#addition
print(x - y)
#subtraction
print(x * y)
#multiplication
print(x / y)
#dvision
print(x ** 2)
#squaring a number

""" 
Sometimes when we're manipulating numbers, we want to work with results again later on.

All we did was print that results of our arithmetic.

The python interpreter is really not that smart, it doesn't remember whgat it prints. So in order for python to rem,ember what it did, you need to save it back into another variable (or itself)
"""
sum = x + y
print(sum)
""" 
So let's keep sum in mind and also add another variable to it.

The equals sign is really just an assingment operatpr and not an equality operator.

common things that happen
    - you'll have a vraiable that you need to update repeatedly
"""

sum = sum + 20 #this is perfectly valid
""" 
Sum is a named place in memory

On the left hand side of the equals sign, we're declaring a variable
On the right hand side, we substitute the value of sum into where called it

sum = x + y
    =15
sum = sum + 20
    15 + 20
sum = 35

"""
print(sum)

""" 
Strings of text:

    - In other programming languages, you have a data type specifically for single characters of text
    - In python, strings of text are all the same data type (string)
"""

name = "Logan Snyder"
#<name of the variable> = <atrtribute>
print(name)

#What if I want to print out "My name is <name>"

""" 
In python, we can do this in two ways.

    - fstrings: format string and it lets specify placeholder values in strings so you can drop in variable
    
"""
print(f"My name is {name}")
