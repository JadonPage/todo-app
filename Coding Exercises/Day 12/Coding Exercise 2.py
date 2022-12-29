password = input("Enter new password: ")


def password_check(password_arg):
    strength = 0
    upper = False
    digit = False
    if len(password_arg) >= 8:
        strength += 1
    for i in password_arg:
        if i.isupper():
            upper = True
    if upper:
        strength += 1
    for i in password_arg:
        if i.isdigit():
            digit = True
    if digit:
        strength += 1
    if strength == 3:
        strong = True
    else:
        strong = False
        if strong:
            return "Strong Password"
        else:
            return "Weak Password"


print(password_check(password))

