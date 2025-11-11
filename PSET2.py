"""
Foundations of Computer Science PSET 2 – String Manipulation
Problem 1 (count.py)
Given the string below
Str = “abbabababbabababababbababababababaaaaababbbbbbababababaababababababababbababaabababaabbabababb
abababababbababababababaaaaababbbbbbababababaababababababababbababaabababaabbabababbabababababbababab
abababaaaaababbbbbbababababaababababababababbababaabababaaaaaababbbbbbababababaababbababbabababbababb
abababababbababababababaaaaababbbbbbababababaababababababababbababaabababaabbabababbabababababbababba
bababababababbababaabababaabbabababbabababababbababababababaaaaababbbbbbababababaabababababababaababa
bbababababababaaaaababbbbbbababababaababababababababbababaabababaaaaaababbbbbbababababaababbababbabab
abbababbbbbbababababaababababababababbababaabababaabbabababbabababababbababababababaaaaababbbbbbababa
babaababababababababbababaabababaaaaaababbbbbbababababaababbababbabababababababaababbababbabababbabab
babababababbababababababaaaaababbbbbbababababaababababababababbababaabababaabbabababbabababababbababb
abababababababbababaabababaabbabababbabbababababababaaaaababbbbbbababababaababababababababbababaababa
baabbabababbabababababbababababababaaaaababbbbbbababababaababababababababbababaabababaaaaaababbbbbbab
abababaababbababbabababbababbabababababbababababababaaaaababbbbbbababababaababababababababbababaababa
baabbabababbabababababbababbabababababababbababaabababaabbabababbababa”

Count how many individual a’s and b’s there are, and print the counts.

Problem 2 (mushrooms.py)
Write a program that: 
•	Asks for the size of a mushroom repeatedly until they type stop
•	Sorts each mushroom into three separate lists, small, medium, large
o	Small mushrooms are mushrooms less than 100 in size
o	Medium mushrooms are mushrooms between 100 and 200 in size
o	Large mushrooms are mushrooms greater than or equal to 200 in size.
•	Print out the lists of each sized mushroom.

Make sure you parse the input appropriately so you don’t get value or type errors, and make sure you parse the input so you typos don’t cause runtime errors. 
Problem 3 (palindrome.py)
A word is considered a palindrome if it is spelled the same forwards and backwards. For example,

“noon”, “racecar”, “taco cat” are palindromes, while “school”, “class”, “room” are not palindromes. 

Your goal is to write a program that can detect if an inputted word is a palindrome. Your program should parse the input such that “Taco Cat” evaluates to true, “        noon” evaluates to true, etc. 

Submission:
Submit each file individually on blackbaud. 
"""

# Lab 3 – Stock Market Evaluation
# No 'with' and no functions

try:
    file1 = open("Day1_20.txt", "r")
    buffer1 = file1.readlines()
    file1.close()

    file2 = open("Day21_40.txt", "r")
    buffer2 = file2.readlines()
    file2.close()

except FileNotFoundError:
    print("Error: One or both input files not found.")
else:
    # --- Convert file lines into data ---
    data1 = {}
    data2 = {}

    for line in buffer1:
        parts = line.strip().split()
        if len(parts) > 1:
            ticker = parts[0]
            prices = []
            for value in parts[1:]:
                try:
                    prices.append(float(value))
                except:
                    print("Error converting value in", ticker)
            data1[ticker] = prices

    for line in buffer2:
        parts = line.strip().split()
        if len(parts) > 1:
            ticker = parts[0]
            prices = []
            for value in parts[1:]:
                try:
                    prices.append(float(value))
                except:
                    print("Error converting value in", ticker)
            data2[ticker] = prices

    # --- Compute averages and write report ---
    try:
        report = open("report.txt", "w")
        report.write("Stock Market Evaluation Report\n")
        report.write("---------------------------------\n\n")

        for ticker in data1:
            prices1 = data1[ticker]
            prices2 = data2[ticker]

            avg1 = sum(prices1) / len(prices1)
            avg2 = sum(prices2) / len(prices2)

            report.write(ticker + ":\n")
            report.write("  Days 1–20 Average: " + str(round(avg1, 2)) + "\n")
            report.write("  Days 21–40 Average: " + str(round(avg2, 2)) + "\n")

            if avg2 > avg1:
                report.write("  Status: Buy (Average Increased)\n\n")
            elif avg2 < avg1:
                report.write("  Status: Sell (Average Decreased)\n\n")
            else:
                report.write("  Status: No Change\n\n")

        report.close()
        print("Report successfully created as report.txt")

    except Exception as e:
        print("Error while writing report:", e)
