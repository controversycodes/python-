# ----------------------------------------
# 📘 Logical Operators (and, or, not)
# ----------------------------------------

# 'and' - both conditions must be True
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")

# 'or' - at least one condition must be True
is_admin = False
is_superuser = True

if is_admin or is_superuser:
    print("Admin access granted.")
else:
    print("Access restricted.")

# 'not' - reverses the boolean value
is_banned = False

if not is_banned:
    print("You can post.")
else:
    print("You are banned.")
