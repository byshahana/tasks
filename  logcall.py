from functools import wraps
from datetime import datetime


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as file:
            file.write(
                f"{datetime.now()} | {func.__name__} | args={args} | kwargs={kwargs}\n"
            )
        return func(*args, **kwargs)

    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def greet(name):
    return f"Hello {name}"


@log_call
def multiply(a, b):
    return a * b


# Call functions a few times
add(2, 3)
add(5, 7)

greet("Alice")
greet("Bob")
greet("Charlie")

multiply(2, 4)
multiply(3, 5)


def read_logs():
    counts = {}

    with open("log.txt", "r") as file:
        for line in file:
            parts = line.split("|")
            function_name = parts[1].strip()

            counts[function_name] = counts.get(function_name, 0) + 1

    print("\nFunction Call Counts:")
    for name, count in counts.items():
        print(f"{name}: {count}")


read_logs()