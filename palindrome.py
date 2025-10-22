#Problem 3 (palindrome.py)

print("Enter a word to see if its a palindrome or type 'stop' to quit.")
check = False
while check == False:
    word = input("Enter a word: ").strip().lower()
    if word == "stop": 
        print("Goodbye")
        check = True

    words = word.split()
    word_no_spaces = "".join(words)

    start = 0
    end = len(word_no_spaces) - 1
    is_palindrome = True

    while start < end:
        if word_no_spaces[start] != word_no_spaces[end]:
            is_palindrome = False
        start += 1
        end -= 1

    if is_palindrome:
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is not a palindrome.")