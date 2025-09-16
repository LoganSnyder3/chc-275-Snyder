""" 
3 angles values as inputs and determine whether or not it is a triangle
"""

angle1 = input("Enter angle 1: ")
angle1 = int(angle1)
angle2 = input("Enter angle 2: ")
angle2 = int(angle2)
angle3 = input("Enter angle 3: ")
angle3 = int(angle3)

#Lets check if its a triangle
#There is no required symbol for and and or, you can just use the words

if (angle1 == 90 and angle2 + angle3 == 90) or (angle2 == 90 and angle1 + angle3 ==90) or (angle3 == 90 and angle1 + angle2 ==90):
    print("This is a triangle")
    
""" 
Our test values worked for 90, 30, 60. We need to find a way to make sure we can have very valid combination of angle 1 2 and 3 create a valid triangle

If you wrap two or more conditionals into one conditional using parentheses, you can reframe the two conditionals to exactly 1 conditional.

Truth table

A       B       A and B
T       F          F
F       T          F
F       F          F
T       T          T

A       B       A or B
T       F          T
F       T          T
T       T          T
F       F          F

This was our lesson on compound conditionals
"""