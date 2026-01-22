#functions.py

#basic function
def foo(): #this is called the function header. 3 parts to the function header.
            #1. Def keyword. This tells the python Interpreter that you are about to specify a funtion
            #2. Function name. This is the name of the routine that you to use.  Ex, foo is the name
            #3. Parameter list. Are your inputs of your function, and they go inside the ()
    print("bar")
    
foo()

def add(x,y):
    #1. def keyword 2. function name: add 3. parameter list: x,y
    #how parameters behave: they are just placeholders for values that we can plug in later.
    print(x + y)
    
add(6,7) #now I want to use the add function
add("foo","bar")