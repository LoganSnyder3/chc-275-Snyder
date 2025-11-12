#Lab 3 - Stock Market Evaluation

file = open("days1_20.txt","r")
buffer = file.readline()
file.close()

msft = buffer[0]
print(buffer)

msft = buffer[0].split(",")
msft.pop(0)

buffer = []

for i in range  (len(msft)):
    line = f"{msft[i]}\n"
    buffer.append()
    
