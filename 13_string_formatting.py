# ----------------------------------------
# 📘 String Formatting Techniques
# ----------------------------------------

name = "Eric"
age = 18

# Old style
print("My name is %s and I am %d years old" % (name, age))

# format() method
print("My name is {} and I am {} years old".format(name, age))

# f-strings (best)
print(f"My name is {name} and I am {age} years old.")
