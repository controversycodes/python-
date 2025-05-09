# ----------------------------------------
# 📘 User Input in Python
# ----------------------------------------

# Taking user input as string
name = input("Enter your name: ")
print("Hello,", name)

# Input as integer
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)

# Input as float
price = float(input("Enter the price: "))
print("Price with tax:", price * 1.18)
# Input as boolean
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
print("Is student:", is_student)
# Input as list
fruits = input("Enter your favorite fruits (comma-separated): ").split(",")
fruits = [fruit.strip() for fruit in fruits]  # Remove extra spaces
print("Favorite fruits:", fruits)