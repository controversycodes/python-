# ----------------------------------------
# 📘 List Comprehension in Python
# ----------------------------------------

# Simple loop
squares = []
for i in range(5):
    squares.append(i ** 2)
print("Squares (normal):", squares)

# List comprehension
squares = [i ** 2 for i in range(5)]
print("Squares (comprehension):", squares)

# With condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print("Even Squares:", even_squares)
# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened Matrix:", flattened)
# ----------------------------------------
# 📘 Dictionary Comprehension in Python