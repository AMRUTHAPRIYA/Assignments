# age_validator.py
# A script with a custom age validation function and exception handling

def validate_age(age):
    # Check if the age is outside the range 0 to 120 (inclusive)
    if not (0 <= age <= 120):
        # Raise a ValueError manually if the age is invalid
        raise ValueError("Invalid age! Age must be between 0 and 120 inclusive.")
    return True

def main():
    try:
        # Prompt the user for their age
        user_input = input("Enter your age: ")
        
        # Convert the input to an integer (this throws a ValueError if they type words)
        age = int(user_input)
        
        # Call our custom validation function
        validate_age(age)
        
        # If no error happened, print success
        print(f"Success: Age {age} is accepted.")
        
    except ValueError as e:
        # Catch any ValueError (either from int() or from our custom validate_age function)
        print(f"Error: {e}")

if __name__ == "__main__":
    main()