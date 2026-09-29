input1 = float(input("Enter the first number: ")) # Use the user to enter the first number and convert it to a float
input2 = float(input("Enter the second number: ")) # Use the user to enter the second number and convert it to a float

# Perform basic arithmetic operations
sum_result = input1 + input2 # Calculate the sum of the two inputs
difference = input1 - input2 # Calculate the difference of the two inputs
product = input1 * input2 # Calculate the product of the two inputs
quotient = input1 / input2 if input2 != 0 else None # Calculate the quotient of the two inputs, handling division by zero

# 2. Ask user to choose an operation

operation = input("Choose an operation (+, -, *, /): ")

    # 3. Perform the chosen operation using conditional statements
    # 4. Prints the result in a user-friendly way.

if operation == "+":  # Perform addition
    print(f"The sum of {input1} and {input2} is {sum_result}")
elif operation == "-":  # Perform subtraction
    print(f"The difference between {input1} and {input2} is {difference}")
elif operation == "*":  # Perform multiplication
    print(f"The product of {input1} and {input2} is {product}")
elif operation == "/":  # Perform division      
    if quotient is not None:
        print(f"The quotient of {input1} divided by {input2} is {quotient}")        
    else:
        print("Division by zero is not allowed.")
else:
        # Handle unsupported operation symbols
        print(f"Error: '{operation}' is an unsupported operation symbol. Please use +, -, *, or /.")

