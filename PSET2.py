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
# No "with" statement version

def read_stock_data(filename):
    """Reads stock data from a text file and returns a dictionary of lists."""
    stock_data = {}
    try:
        file = open(filename, 'r')
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                ticker = parts[0]
                try:
                    prices = [float(x) for x in parts[1:]]
                    stock_data[ticker] = prices
                except ValueError:
                    print("Error: Could not convert prices to numbers for", ticker)
        file.close()
    except FileNotFoundError:
        print("Error: File", filename, "not found.")
        return None
    except Exception as e:
        print("Unexpected error while reading", filename, ":", e)
        return None
    else:
        return stock_data

def calculate_average(prices):
    """Calculates the average of a list of numbers."""
    if not prices:
        return 0
    return sum(prices) / len(prices)

def generate_report(day1_file, day21_file, report_file):
    """Generates a stock comparison report."""
    try:
        data1 = read_stock_data(day1_file)
        data2 = read_stock_data(day21_file)

        if data1 is None or data2 is None:
            print("Could not generate report due to missing data.")
            return

        report = open(report_file, 'w')
        report.write("Stock Market Evaluation Report\n")
        report.write("---------------------------------\n\n")

        for ticker in data1.keys():
            avg1 = calculate_average(data1[ticker])
            avg2 = calculate_average(data2.get(ticker, []))

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
        print("Report successfully generated as", report_file)

    except Exception as e:
        print("Error while generating report:", e)

# --- Run Program ---
generate_report('Day1_20.txt', 'Day21_40.txt', 'report.txt')
.