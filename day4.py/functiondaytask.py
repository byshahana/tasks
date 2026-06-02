class InvalidMarkError(Exception):
    pass


def calculate_grade(name, *marks):
    if len(marks) == 0:
        raise ValueError("No marks provided")

    for mark in marks:
        if mark < 0 or mark > 100:
            raise InvalidMarkError("Marks must be between 0 and 100")

    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"

    return avg, grade


def generate_report(students):
    print(f"{'Name':<10} {'Average':<10} {'Grade':<5}")
    print("-" * 30)

    for student in students:
        name = student[0]
        marks = student[1:]

        try:
            avg, grade = calculate_grade(name, *marks)
            print(f"{name:<10} {avg:<10.2f} {grade:<5}")

        except Exception as e:
            print(f"{name:<10} Error: {e}")


students = [
    ("Rahul", 90, 95, 85),      # Valid
    ("Anu", 150, 80, 70),       # Invalid mark
    ("John",),                  # Empty marks
    ("Sara", 75, 60, -5)        # Mixed valid and invalid
]

generate_report(students)