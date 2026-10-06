# ==========================================
# Script 3: safe_calc.py
# Purpose: Practice robust exception handling in Python
# ==========================================

def perform_safe_division():
    # Prompt the user to enter the numerator
    num_str = input("Enter a numerator (number): ")
    
    # Prompt the user to enter the denominator
    den_str = input("Enter a denominator (number): ")
    
    try:
        # Attempt to convert both user string inputs into floating-point numbers
        numerator = float(num_str)
        denominator = float(den_str)
        
        # Attempt division; this will raise a ZeroDivisionError if denominator is 0
        result = numerator / denominator
        
    except ValueError:
        # Executes if the user enters letters or symbols instead of valid numbers
        print("❌ Error: Invalid input! Please enter valid numeric characters.")
    except ZeroDivisionError:
        # Executes if the denominator evaluates to zero
        print("❌ Error: Division by zero is mathematically impossible.")
    else:
        # Executes only if no exceptions occurred inside the try block
        print(f"✅ Success! {numerator} divided by {denominator} equals {result}")
    finally:
        # Executes unconditionally whether an error occurred or not
        print("🔒 Execution of the safe division check is complete.\n")

# Run the division function when executed directly
if __name__ == "__main__":
    perform_safe_division()