# ----------------------------------------
# 📘 Exception Handling in Python
# ----------------------------------------

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
    print("❌ You can't divide by zero.")
except ValueError:
    print("❌ Enter a valid number.")
finally:
    print("✅ Done with error handling.")
