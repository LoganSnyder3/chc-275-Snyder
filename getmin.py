def getmin(userlist):
    min_value = userlist[0]

    i = 1
    while i < len(userlist):
        if userlist[i] < min_value:
            min_value = userlist[i]
        i += 1

    return min_value
    
print(getmin([1,2,3,4]))
print(getmin([4,2,1,3]))
print(getmin([10,20,30,40]))
