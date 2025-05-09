# ----------------------------------------
# 📘 Functions and Recursion - Coming Soon
# ----------------------------------------

# Function definition
def say_hello(name):
    print("Hello,", name)

say_hello("Eric")

# Recursive function: factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
