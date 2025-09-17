""" 
Review of control structures that we have so far:
    - Sequential (line after line execution)
    - Branching (if-elif-else)
    - Repetition (which we will cover today).
"""

"""
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
"""

#This is how we would print 10 numbers with what we know

""" 
There are 3 ways to repeat a code segment:
    - While loops (This is something attainable right now)
    - For Loops (Requires knowledge of lists)
    - Recursion (We will not see until the second semester)\

while loops are the easiest and the syntax is

while <exit condition>
    <repeated block>

exit conditions are conditional statements. So they have to evaluate to either true or false

the routine for a while loop

1) checks the exit condition
2) if the exit condition is not satisfied, perform the code block underneath
3) go back to step 1
"""

""" 
x = 1
while x <= 10:
    print(x)
"""
    
#Our exit condition is never satisfied

""" 
When something runs forever, the program will eventually halt and throw an error called a "stack overflow"

What is a stack overflow?

Your computer has a component called the Random Access Memory. 
RAM is responsible for holding all of the information corresponding to processes that are running currently.

When a python program is ran, what the python interpreter will do is allocated partitions of RAM to two different collections.

    - Stack: A fixed amount of memory for things like function calls and basic variable assignment
            (you have a limited memory budget for your program)
    - Heap: A dynamically changing amount of memory for things like complex data structures
            (You have a changing memory budget for your program)
"""

x = 1
while x <= 10:
    print(x)
    #We want x to satisfy the exit condition at some point. The natural option is to keep adding 1 to x
    #Two ways to do it, one way is a contraction, the other way is more verbose
    
    #x = x + 1
    
    x += 1

nums = [1,2,3,4,5,6,7,8,9,19]
x = 0
sum = 0
while x < len(nums):
    sum += nums[x]
    x += 1
    
print(f"the sum is {sum}")

""" 
How are looping statements useful?

From a program design standpoint, they also allow us to repeat an entire program until we quit.

There's a boolean data type, we can set variables equal to True or False
"""

check = False
        #Make sure you use capital F
while check == False:
    print("option 1")
    print("option 2")
    print("option 3")
    option = input("Select your option or type quit to exit: ")
    if option == "1":
        print(1)
    elif option == "2":
        print(2)
    elif option == "3":
        print(3)
    elif option == "quit":
        check = True
    
    
