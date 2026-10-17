# Task 2: Multiplier Closure
# A closure is an inner function that remembers variables from its outer function even after it has finished.

def make_multiplier(factor):
    """Returns a closure function that multiplies any input by the given factor."""
    
    # This inner function remembers what 'factor' was set to
    def multiplier(x):
        return x * factor
        
    return multiplier

# Test code
if __name__ == "__main__":
    print("--- Testing Multiplier Closures ---")
    
    # Create two specific multiplier functions
    times3 = make_multiplier(3)   # Remembers factor = 3
    times10 = make_multiplier(10) # Remembers factor = 10
    
    input_val = 7
    # Test them out
    print(f"times3({input_val}) = {times3(input_val)}")
    print(f"times10({input_val}) = {times10(input_val)}")