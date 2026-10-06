# logic_bits.py

print("=== PART A: Logical Operators ===")
# Simulating boolean inputs
bool1 = True
bool2 = False

print(f"Input 1: {bool1}, Input 2: {bool2}")
print(f"bool1 and bool2: {bool1 and bool2}")
print(f"bool1 or bool2: {bool1 or bool2}")
print(f"not bool1: {not bool1}")

print("\n=== PART B: Bitwise Operators ===")
a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(f"Integer a = {a} (Binary: {bin(a)})")
print(f"Integer b = {b} (Binary: {bin(b)})")
print("-" * 35)

# Bitwise AND (&)
print(f"a & b  = {a & b} \t(Binary: {bin(a & b)})")

# Bitwise OR (|)
print(f"a | b  = {a | b} \t(Binary: {bin(a | b)})")

# Bitwise XOR (^)
print(f"a ^ b  = {a ^ b} \t(Binary: {bin(a ^ b)})")

# Bitwise NOT (~) -> formula: ~x = -(x + 1)
print(f"~a     = {~a} \t(Binary: {bin(~a)})")

# Bitwise Left Shift (<<)
print(f"a << 1 = {a << 1} \t(Binary: {bin(a << 1)})")

# Bitwise Right Shift (>>)
print(f"a >> 1 = {a >> 1} \t(Binary: {bin(a >> 1)})")