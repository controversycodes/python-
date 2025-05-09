# ----------------------------------------
# 📘 File Handling - Coming Soon
# ----------------------------------------

# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Hello, file world!")

# Reading from a file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:", content)
# Appending to a file
with open("sample.txt", "a") as f:
    f.write("\nAppending this line.")
# Reading the updated file
with open("sample.txt", "r") as f:
    content = f.read()
    print("Updated file content:", content)
# File handling with context manager
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())  # Print each line without extra spaces