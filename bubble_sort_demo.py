# bubble_sort_demo.py

# Use a fixed unsorted list of integers
unsorted_list = [64, 25, 12, 22, 11]

print("Original Unsorted List:", unsorted_list)
print("-" * 40)

n = len(unsorted_list)

# Outer loop for each pass through the list
for i in range(n):
    swapped = False
    
    # Inner loop for comparing adjacent elements
    # With each full pass, the largest element bubbles to the end, so we can reduce range
    for j in range(0, n - i - 1):
        if unsorted_list[j] > unsorted_list[j + 1]:
            # Swap if elements are in the wrong order
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
            swapped = True
            
    # Print the list progress after each pass of the outer loop
    print(f"Pass {i + 1}: {unsorted_list}")
    
    # Optimization: if no swaps occurred during this pass, the list is already sorted
    if not swapped:
        break

print("-" * 40)
print("Final Sorted List:", unsorted_list)