# ----------------------------------------
# 📘 Python Data Types - Explained with Examples
# ----------------------------------------

# 🔹 1. Integer (int): Whole numbers, positive or negative
x = 10
y = -5
print("Integer:", x, y)

# 🔹 2. Float (float): Numbers with decimal point
pi = 3.14159
temp = -2.5
print("Float:", pi, temp)

# 🔹 3. String (str): Text enclosed in single or double quotes
name = "Alice"
greeting = 'Hello, world!'
print("String:", name, greeting)

# 🔹 4. Boolean (bool): True or False
is_active = True
is_logged_in = False
print("Boolean:", is_active, is_logged_in)

# 🔹 5. List: Ordered, mutable (changeable) collection of items
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# Accessing list item
print("First fruit:", fruits[0])

# 🔹 6. Tuple: Ordered, **immutable** collection of items
coordinates = (10.0, 20.0)
print("Tuple:", coordinates)

# 🔹 7. Set: Unordered collection of **unique** items
unique_numbers = {1, 2, 3, 3, 4}
print("Set (duplicates removed):", unique_numbers)

# 🔹 8. Dictionary (dict): Key-Value pairs
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
print("Dictionary:", person)
print("Name from dict:", person["name"])

# 🔹 9. NoneType: Represents the absence of a value
nothing = None
print("NoneType:", nothing)

# ----------------------------------------
# 🔁 You can check type using `type()` function
print("Type of 'pi':", type(pi))
print("Type of 'fruits':", type(fruits))



# ----------------------------------------
# Variables in Python
# ----------------------------------------

# A variable stores data in memory
age = 18               # integer
name = "Eric"          # string
height = 5.9           # float
is_student = True      # boolean

# Printing all variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Variable reassignment
age = 19
print("Updated Age:", age)
