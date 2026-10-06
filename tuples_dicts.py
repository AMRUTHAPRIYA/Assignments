# ==========================================
# Script 2: tuple_dict_demo.py
# Purpose: Practice working with tuples and dictionaries
# ==========================================

# 1. Create a tuple containing fixed personal or geographic data (immutable)
user_coordinates = (34.0522, -118.2437)
print(f"Original Tuple coordinates: {user_coordinates}")

# Note: Attempting to modify a tuple (e.g., user_coordinates[0] = 35.0) 
# would trigger a TypeError because tuples are immutable.

# 2. Create a dictionary representing a student or record
student_record = {
    "name": "Haripriya",
    "track": "Software Engineering",
    "module": "ALAB 351.4",
    "active": True
}
print("\nOriginal Dictionary Record:")
print(student_record)

# 3. Access a specific dictionary value using its key
print(f"Student Name: {student_record['name']}")

# 4. Add a new key-value pair to the dictionary
student_record["grade"] = "A"
print(f"Added grade key: {student_record}")

# 5. Modify an existing value in the dictionary
student_record["active"] = False
print(f"Updated 'active' status: {student_record}")

# 6. Iterate through dictionary keys and values using .items()
print("\nIterating through dictionary items:")
for key, value in student_record.items():
    print(f"Key: {key} --> Value: {value}")