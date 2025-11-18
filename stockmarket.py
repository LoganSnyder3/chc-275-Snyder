#Lab 3 - Stock Market Evaluation

try:
    file = open("days1_20.txt", "r")
    buffer1 = file.readlines()
except FileNotFoundError:
    print("days1_20.txt not found.")
    buffer1 = []
except Exception as e:
    print("Error reading days1_20.txt:", e)
    buffer1 = []
else:
    file.close()

try:
    file = open("days21_40.txt", "r")
    buffer2 = file.readlines()
except FileNotFoundError:
    print("days21_40.txt not found.")
    buffer2 = []
except Exception as e:
    print("Error reading days21_40.txt:", e)
    buffer2 = []
else:
    file.close()

line = buffer1[0].strip().split(",")
msft1 = []
i = 1
while i < len(line):
    msft1.append(int(line[i]))
    i += 1

line = buffer1[1].strip().split(",")
amzn1 = []
i = 1
while i < len(line):
    amzn1.append(int(line[i]))
    i += 1

line = buffer1[2].strip().split(",")
nvda1 = []
i = 1
while i < len(line):
    nvda1.append(int(line[i]))
    i += 1


line = buffer2[0].strip().split(",")
msft2 = []
i = 1
while i < len(line):
    msft2.append(int(line[i]))
    i += 1

line = buffer2[1].strip().split(",")
amzn2 = []
i = 1
while i < len(line):
    amzn2.append(int(line[i]))
    i += 1

line = buffer2[2].strip().split(",")
nvda2 = []
i = 1
while i < len(line):
    nvda2.append(int(line[i]))
    i += 1

try:
    report = open("report.txt", "w")

    # MSFT
    sum1 = 0
    i = 0
    while i < 20:
        sum1 += msft1[i]
        i += 1
    avg1 = sum1 // 20

    sum2 = 0
    i = 0
    while i < 20:
        sum2 += msft2[i]
        i += 1
    avg2 = sum2 // 20

    report.write("MSFT\n")
    report.write("  Days 1_20 Average: " + str(avg1) + "\n")
    report.write("  Days 21_40 Average: " + str(avg2) + "\n")
    if avg2 > avg1:
            report.write("  Recommendation: BUY\n\n")
    else:
            report.write("  Recommendation: DO NOT BUY\n\n")

    # AMZN
    sum1 = 0
    i = 0
    while i < 20:
        sum1 += amzn1[i]
        i += 1
    avg1 = sum1 // 20

    sum2 = 0
    i = 0
    while i < 20:
        sum2 += amzn2[i]
        i += 1
    avg2 = sum2 // 20

    report.write("AMZN\n")
    report.write("  Days 1_20 Average: " + str(avg1) + "\n")
    report.write("  Days 21_40 Average: " + str(avg2) + "\n")
    if avg2 > avg1:
        report.write("  Recommendation: BUY\n\n")
    else:
        report.write("  Recommendation: DO NOT BUY\n\n")

    # NVDA
    sum1 = 0
    i = 0
    while i < 20:
        sum1 += nvda1[i]
        i += 1
    avg1 = sum1 // 20

    sum2 = 0
    i = 0
    while i < 20:
        sum2 += nvda2[i]
        i += 1
    avg2 = sum2 // 20

    report.write("NVDA\n")
    report.write("  Days 1_20 Average: " + str(avg1) + "\n")
    report.write("  Days 21_40 Average: " + str(avg2) + "\n")
    if avg2 > avg1:
        report.write("  Recommendation: BUY\n\n")
    else:
        report.write("  Recommendation: DO NOT BUY\n\n")

except Exception as e:
    print("Error writing report.txt:", e)
else:
    report.close()
    print("Report created: report.txt")
