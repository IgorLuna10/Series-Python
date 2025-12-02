# password = "azerty123"
# print(len(password))

# password = "QwerTY!@#"
# for caracter in password:
#     print(caracter)

# c = "A"
# print(c.islower())
# print(c.isupper())

# d= "5"
# print(d.isdigit())

password = input("Enter your password: ")

if len(password) < 8:
    print("Your password is too short and not valid")

else:
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        print("Your password is valid")
    if not has_upper and not has_lower and has_digit:
        print("Your password is not valid, it must contain at least one upper case letter and one digit")
    if has_upper and not has_lower and not has_digit:
        print("Your password is not valid, it must contain at least one lower case letter and one digit")
    if not has_upper and has_lower and not has_digit:
        print("Your password is not valid, it must contain at least one upper case letter and one digit")
    if has_upper and has_lower and not has_digit:
        print("Your password is not valid, it must contain at least one digit")
    if has_upper and not has_lower and has_digit:
        print("Your password is not valid, it must contain at least one lower case letter")
    if not has_upper and has_lower and has_digit:
        print("Your password is not valid, it must contain at least one upper case letter")
