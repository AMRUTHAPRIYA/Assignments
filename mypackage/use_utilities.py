# Import custom module from the package
from mypackage import utilities

# Test the greet function
user_name = "Haripriya"
greeting_message = utilities.greet(user_name)
print(greeting_message)

# Test the factorial function
number = 5
fact_result = utilities.factorial(number)
print(f"The factorial of {number} is: {fact_result}")
