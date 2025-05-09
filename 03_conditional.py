# ----------------------------------------
# 📘 Conditional Statements in Python
# ----------------------------------------

age = 17

# Simple if condition
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# elif condition
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Nested if
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome Admin!")
    else:
        print("Welcome User!")
else:
    print("Please log in.")
