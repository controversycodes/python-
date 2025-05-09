# ----------------------------------------
# 📘 Loops in Python - for & while
# ----------------------------------------

# 🔁 for loop - iterate through a list
animals = ["cat", "dog", "cow"]

for animal in animals:
    print("Animal:", animal)

# Range loop
for i in range(1, 6):
    print("Number:", i)

# 🔁 while loop - runs as long as condition is True
count = 1
while count <= 5:
    print("Counting:", count)
    count += 1
# Infinite loop (use with caution)
# while True:
#     print("This will run forever unless stopped!")
#     break  # Use break to exit the loop
# ----------------------------------------
# 📘 Loop Control Statements