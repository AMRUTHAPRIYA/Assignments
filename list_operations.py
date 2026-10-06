# list_operations.py

# 1. Create a list of at least 5 integers
numbers = [42, 15, 8, 23, 4]

print("Original list:")
print(numbers)
print("-" * 30)

# 2. Use sorted() without modifying the original list
print("Sorted list (using sorted()):")
print(sorted(numbers))
print("Original list remains unchanged:", numbers)
print("-" * 30)

# 3. Use .sort() to sort the list in place
numbers.sort()
print("List after in-place sort (.sort()):")
print(numbers)
print("-" * 30)

# 4. Add a new element using append()
numbers.append(99)
print("Updated list after appending 99:")
print(numbers)
print("-" * 30)

# 5. Remove an element (e.g., remove value 15)
numbers.remove(15)
print("List after removing 15:")
print(numbers)
print("-" * 30)

# 6. Reverse the list using reverse()
numbers.reverse()
print("Reversed list:")
print(numbers)
