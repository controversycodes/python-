# ----------------------------------------
# 📘 *args and **kwargs in Python
# ----------------------------------------

# ✅ *args allows you to pass multiple non-keyword (positional) arguments
# These arguments are received as a tuple
def example_args(*args):
    print("Received args:", args)

example_args(1, 2, 3)
# Output: Received args: (1, 2, 3)

# ✅ Use-case: When number of inputs is unknown
def add_all(*args):
    return sum(args)

print("Sum:", add_all(5, 10, 15))  # Output: 30

# ✅ You can unpack a list or tuple using * when calling the function
nums = [1, 2, 3]
print("Sum from list:", add_all(*nums))  # Output: 6


# ✅ **kwargs allows you to pass multiple keyword arguments
# These arguments are received as a dictionary
def example_kwargs(**kwargs):
    print("Received kwargs:", kwargs)

example_kwargs(name="Eric", age=18)
# Output: Received kwargs: {'name': 'Eric', 'age': 18}

# ✅ Use-case: When you want to accept optional named arguments
def greet_user(**kwargs):
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello, Guest!")

greet_user(name="Eric")  # Output: Hello, Eric!
greet_user()             # Output: Hello, Guest!

# ✅ You can unpack a dictionary using ** when calling the function
user_data = {"name": "Ali", "age": 22}
greet_user(**user_data)  # Output: Hello, Ali!


# ✅ You can combine *args and **kwargs in a single function
def full_example(a, b, *args, **kwargs):
    print("Required a and b:", a, b)
    print("Additional args:", args)
    print("Additional kwargs:", kwargs)

full_example(1, 2, 3, 4, name="Zaid", city="Delhi")

# Output:
# Required a and b: 1 2
# Additional args: (3, 4)
# Additional kwargs: {'name': 'Zaid', 'city': 'Delhi'}
