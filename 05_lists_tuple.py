# ----------------------------------------
# 📘 Lists and Tuples in Python
# ----------------------------------------

# 🔸 List - mutable, ordered collection
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Access
print("First fruit:", fruits[0])

# Modify
fruits[1] = "orange"
print("Modified List:", fruits)

# Append
fruits.append("grape")
print("After append:", fruits)

# Remove
fruits.remove("apple")
print("After removal:", fruits)

# 🔸 Tuple - immutable, ordered collection
colors = ("red", "green", "blue")
print("Colors:", colors)

# Accessing tuple
print("First color:", colors[0])

# Note: You cannot change tuple values
# colors[0] = "yellow" → ❌ TypeError
