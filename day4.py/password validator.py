class WeakPasswordError(Exception):
    pass


def validate_password(password):

    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long")

    if not any(char.isdigit() for char in password):
        raise WeakPasswordError("Password must contain a digit")

    if not any(char.isupper() for char in password):
        raise WeakPasswordError("Password must contain an uppercase letter")

    return "Password is valid"


try:
    password = input("Enter password: ")
    print(validate_password(password))

except WeakPasswordError as e:
    print(e)