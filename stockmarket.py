#Lab 3 - Stock Market Evaluation

try:
    file1 = open("days1_20.txt", "r")
    buffer1 = file1.readlines()
    file1.close()
    
    file2 = open("days21_40.txt", "r")
    buffer2 = file2.readlines()
    file2.close()

except FileNotFoundError:
    print("One or both files not found")
else:
    data1 = {}
    data2 = {}

    for line in buffer1:
        parts = line.strip().split()
        if len(parts) > 1:
            ticker = parts[0]
            prices = []
            for value in parts[1]:
               