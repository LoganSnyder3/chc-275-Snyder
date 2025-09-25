""" 
If I wanted a bunch of realted data points, the only way I can do that currently is by creating a bunch of individual variables.
"""

num1 = 10
num2 = 20

""" 
What happens when our data set is 100 data points long? Creating individual varibables is a really unwieldy way to handle this. We need some sort of
way to aggregate related data points together.

We can do this in python using lists.

Lists = linear, ordered collections of objects under one variable name (under one memory address)
      = lists are also variables
      
<name of the list> = [<member attributes>]
"""

mylist = [5, 10, 15, 20,]
    #this creates our list
print(mylist)

""" 
index = the numerical position of the object within the list
"""

print(mylist[0])

""" 
Counting in computer science starts at 0. Really, the first element is index = 0. accessing elements from a list behaves
exactly like a variable would.  
"""

print(mylist[0] * mylist[3])

for num in mylist:
    num = num + 5

print(mylist)


i = 0
while i <= 3:
    mylist[i] = mylist[i] + 5
    i = i + 1
    
print(mylist)







