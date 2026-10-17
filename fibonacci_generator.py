# Task 1: Fibonacci Generator
# A generator uses 'yield' to return values one at a time, which saves computer memory.

def gen_fibonacci(n):
    """Generates the first n numbers of the Fibonacci sequence."""
    # If the user asks for 0 or negative numbers, stop immediately
    if n <= 0:
        return
    
    # The first two starting numbers in Fibonacci
    a = 0
    b = 1
    
    # Loop n times to generate each number
    for _ in range(n):
        yield a            # Give the current number back to the loop
        # Update our numbers: 'a' becomes 'b', and 'b' becomes the sum of the previous two
        a, b = b, a + b

# Test code
if __name__ == "__main__":
    n_terms = 10
    print(f"--- Fibonacci Sequence (First {n_terms} Numbers) ---")
    
    # Loop through the generator and print each term with a clean label
    for index, value in enumerate(gen_fibonacci(n_terms), start=1):
        print(f"Fibonacci term {index}: {value}")