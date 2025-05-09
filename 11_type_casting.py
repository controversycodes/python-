# ----------------------------------------
# 📘 Type Casting in Python
# ----------------------------------------

# String to int
num_str = "10"
num_int = int(num_str)
print(num_int + 5)

# Int to string
age = 18
print("Age: " + str(age))

# Float to int
pi = 3.14
whole = int(pi)
print("Converted:", whole)

# Automatic casting
x = 5    # int
y = 2.5  # float
z = x + y
print("Result:", z)  # 7.5
# Note: Python automatically converts int to float when needed