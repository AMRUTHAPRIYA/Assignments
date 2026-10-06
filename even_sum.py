# even_sum.py

# --- Approach 1: Using a For Loop ---
total_sum_for = 0
for num in range(1, 51):  # Iterates from 1 to 50
    if num % 2 == 0:      # Checks if the number is even
        total_sum_for += num

print(f"The sum of even numbers from 1 to 50 is {total_sum_for} (using a for loop).")


# --- Approach 2: Using a While Loop ---
total_sum_while = 0
current_num = 1

while current_num <= 50:
    if current_num % 2 == 0:
        total_sum_while += current_num
    current_num += 1

print(f"The sum of even numbers from 1 to 50 is {total_sum_while} (using a while loop).")

# --- Commentary ---
# Both loop versions produce the exact same result (650). 
# The 'for' loop is generally cleaner and less prone to infinite loops because 
# the iteration and incrementing are handled automatically by the range() function.
# The 'while' loop, on the other hand, requires manual handling of the loop variable and is more prone to errors if not managed carefully.      

