# ----------------------------------------
# 📘 Strings in Python
# ----------------------------------------

# Creating strings
greet = "Hello"
name = "Eric"

# String concatenation
message = greet + " " + name
print("Concatenated Message:", message)

# f-strings (recommended way)
print(f"My name is {name} and I say {greet}!")

# Common string functions
text = "  Python Is Awesome  "

print("Original:", text)
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Stripped:", text.strip())        # removes spaces
print("Length:", len(text))
print("Replaced:", text.replace("Awesome", "Powerful"))

# Accessing characters
print("First letter:", text[0])
print("Last letter:", text[-1])
print("Slice (2nd to 5th):", text[1:5])  # slicing
print("Slice (from 2nd):", text[1:])     # slicing
print("Slice (up to 5th):", text[:5])     # slicing
print("Slice (last 5):", text[-5:])     # slicing
print("Slice (2nd to 5th, step 2):", text[1:5:2])  # slicing with step
print("Slice (last 5, step 2):", text[-5::2])  # slicing with step
print("Slice (last 5, step -1):", text[-5::-1])  # slicing with step
print("Slice (last 5, step -2):", text[-5::-2])  # slicing with step
