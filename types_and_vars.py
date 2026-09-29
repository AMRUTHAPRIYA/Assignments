#1. Declares a variable name and assigns it your name as a string
#2. Declares a variable age and assigns it your age as an integer.
#3. Declares a variable height and assigns it a floating-point number representing your height in meters.


name = "Haripriya"
age = 38
height = 1.52  # in Meters


future_age = age + 10

# 4. Prints a sentence introducing yourself

print(f"Hello, my name is {name}. I am  {age} years old. In 10 years, I will be {future_age} years old. I am {height} meters tall.")

# After the introduction sentence, add code that calculates what your age will be in 5 years and print a sentence stating that. For example: "In 5 years, I will be 25 years old."  

future_age_in_5_years = age + 5
print(f"In 5 years, I will be {future_age_in_5_years} years old.")

# Calculate the area of a rectangle with width = 5.5 and height = 2 (you can hardcode these numbers or store them in variables). Print the result in a formatted sentence: "The area of a 5.5 x 2 rectangle is 11.0
 
height = 4
width = 2
area = width * height
print(f"The area of rectangle is {height} * {width} = {area}")  # The area of a 4 x 2 rectangle is 8

# Demonstrate the use of at least two different arithmetic operators (e.g., +, -, *, /, //, or %) and one string concatenation or repetition (e.g., using + to join strings or * to repeat a string).

Box_cookies = 12

total_cookies = 43

Boxes_Needed = total_cookies // Box_cookies
print(f"Number of boxes needed {Boxes_Needed}")  # Demonstrates the use of the // operator for integer division
# Demonstrates the use of the % operator for finding the remainder
remaining_cookies = total_cookies % Box_cookies
print(f"Remaining cookies after filling boxes: {remaining_cookies}")  # Demonstrates the use of the % operator for finding the remainder

# Demonstrates string concatenation
greeting = "Hello, " + name + "!"
print(greeting)  # Demonstrates string concatenation using +


#Exponentiation (**) — The Growing Bacterial Culture


Initial_bacteria = 100

growth_factor = 2  # Bacteria double every hour
hours = 5
final_bacteria = Initial_bacteria * (growth_factor ** hours)
print(f"After {hours} hours, the bacterial culture will have {final_bacteria} bacteria.")  # Demonstrates the use of the ** operator for exponentiation

