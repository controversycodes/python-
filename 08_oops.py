# ----------------------------------------
# 📘 Basic OOP (Object-Oriented Programming) - In Progress
# ----------------------------------------

# A simple class and object example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I’m {self.name} and I’m {self.age} years old.")

# Creating object
p1 = Person("Eric", 18)
p1.greet()
p2 = Person("John", 25)
p2.greet()
# Creating another object
p3 = Person("Alice", 30)
p3.greet()
# Creating another object
p4 = Person("Bob", 22)
p4.greet()