# 1. Ask the user to input a numeric grade
grade = float(input("Enter your numeric grade (0-100): "))

# 2. Use an if-elif-else structure with boundary/edge case coverage
if 90 <= grade <= 100:
    letter_grade = "A"
elif 80 <= grade < 90:
    letter_grade = "B"
elif 70 <= grade < 80:
    letter_grade = "C"
elif 60 <= grade < 70:
    letter_grade = "D"
elif 0 <= grade < 60:
    letter_grade = "F"
else:
    letter_grade = "Invalid"

# 3. Print the letter grade
if letter_grade != "Invalid":
    print(f"Your grade is: {letter_grade}")

# 4. Include a final conditional message (passing vs trying again)
    message = "Congratulations on your great performance!" if letter_grade in ["A", "B", "C"] else "Keep your head up and try again, you've got this!"
    print(message)
else:
    print("Please enter a valid grade between 0 and 100.")
    