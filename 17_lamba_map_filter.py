# ----------------------------------------
# 📘 Lambda, map, filter in Python
# ----------------------------------------

# Lambda (anonymous function)
square = lambda x: x * x
print("Square of 5:", square(5))

# map() with lambda
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print("Doubled:", doubled)

# filter() with lambda
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even)
