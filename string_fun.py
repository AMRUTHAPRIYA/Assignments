#Prompts the user for a word.

word = input("Enter a word: ") # Prompt the user to enter a word
print(f"You entered: {word}") # Display the entered word back to the user

#Prints the length of the word.

word_length = len(word)
print(f"Length of the word: {word_length}")

# 3. Print the word in all uppercase using .upper()
uppercase_word = word.upper()
print(f"Uppercase: {uppercase_word}")

# 4. Print the word repeated 3 times using string multiplication (*)
repeated_word = (word + " ") * 3
print(f"Repeated 3 times: {repeated_word}")