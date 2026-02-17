#Name: Logan Snyder
#Section: 2
#Description: Lab 4

import math

def getList():
    userList: []

    print("Welcome to the List Statistics Calculator")
    print("Enter a list of integers or 'q' to end the list.")

    while True:
        value = input("Enter an integer: ")
        if value.lower() == 'q':
            break
        userList.append(int(value))
    return userList

def printMenu():
    print("\nPlease choose the statistic you would like to calculate.")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Standard Deviation")
    print("6. Exit")

def getMean(userList):
    total = 0
    for num in userList:
        total += num
    return total / len(userList)

def getMedian(userList):
    userList = sorted(userList)
    n = len(userList)

    if n % 2 == 1:
        return userList[n // 2]
    else:
        mid1 = userList[n //2]
        mid2 = userList[n // 2 - 1]
        return (mid1 + mid2) / 2
def getMin(userList):
    minimum = userList[0]
    for num in userList:
        if num < minimum:
            minimum = num
    return minimum

def getMax(userList):
    maximum = userList[0]
    for num in userList:
        if num > maximum:
            maximum = num
    return maximum

def getStdDev(userList):
    mean = getMean(userList)
    n = len(userList)

    SSE = 0

    for current in userList:
        SSE = SSE + (current - mean) ** 2

    SSE = SSE / n

    return math.sqrt(SSE)

def main():
    userList = getList()

    while True:
        printMenu()
        choice = int(input("Please enter your choice, or 6 to exit: "))
        if choice == 6:
            break
        elif choice == 1:
            print("The minimum value is:", getMin(userList))
        elif choice == 2:
            print("The maximum value is:", getMax(userList))
        elif choice == 3:
            print("The mean value is:", getMean(userList))
        elif choice == 4:
            print("The median value is:", getMedian(userList))
        elif choice == 5:
            print("The Standard Deviation is:", getStdDev(userList))
        else:
            print("Invalid choice.")
            
    if __name__ == "__main__":
        main()
