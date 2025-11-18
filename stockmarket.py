#Lab 3 - Stock Market Evaluation

file = open("days1_20.txt","r")
buffer = file.readline()
file.close()
print(buffer)

msft = buffer[0].split(",")
msft.pop(0)

amzn = buffer[1]
nvda = buffer[2]

print(msft)

try:
    for i in range(len(msft)):
        msft[i] = int(msft[i])
except ValueError:
    print("Must be numbers")

