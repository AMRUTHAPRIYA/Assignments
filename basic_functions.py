# ==========================================
# Script 1: basic_functions.py
# Purpose: Practice writing and calling functions in Python
# ==========================================

# 1. Define a function greet_user() that takes a name (string) as a parameter
def greet_user(name=""):
    # Check if the name parameter is empty or evaluates to False
    if not name:
        # Print a generic welcome message if no name is provided
        print("Hello! Welcome!")
    else:
        # Print a personalized welcome message using an f-string
        print(f"Hello, {name}! Welcome!")

# 2. Define a function add_two_numbers() that returns the sum of two numbers
def add_two_numbers(a, b):
    # Return the sum of parameters a and b to the caller
    return a + b

# 3. Define a function is_even() that returns True if num is even, False otherwise
def is_even(num):
    # Check if the remainder when dividing by 2 is zero
    if num % 2 == 0:
        return True
    else:
        return False

# 4. In the main part of the script, demonstrate each function
if __name__ == "__main__":
    print("--- Demonstrating greet_user() ---")
    # Call greet_user with a sample name argument
    greet_user("Haripriya")
    # Call greet_user without an argument to trigger the default fallback
    greet_user()
    
    print("\n--- Demonstrating add_two_numbers() ---")
    # Store the returned sum of 15 and 27 in a variable
    sum_result = add_two_numbers(15, 27)
    # Print the calculated result
    print(f"The sum of 15 and 27 is: {sum_result}")
    
    print("\n--- Demonstrating is_even() ---")
    # Check if 4 is even
    print(f"Is 4 even? {is_even(4)}")
    # Check if 7 is even
    print(f"Is 7 even? {is_even(7)}")