# ----------------------------------------
# 📘 Dictionaries and Sets
# ----------------------------------------

# Dictionary
person = {"name": "Eric", "age": 18}

print("Name:", person["name"])
print("Age:", person.get("age"))

person["city"] = "Delhi"
print("Updated:", person)

for key, value in person.items():
    print(f"{key} → {value}")

# Set - unique items
nums = {1, 2, 3, 2, 1}
print("Set:", nums)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)
# Set comprehension
squares = {x ** 2 for x in range(10)}
print("Squares Set:", squares)
# Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(5)}
print("Squares Dict:", squares_dict)
# Nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print("Nested Dictionary:", nested_dict)