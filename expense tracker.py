import json


# Add Expense
def add_expense(category, amount):
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []

    expenses.append({
        "category": category,
        "amount": amount
    })

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expense added successfully!")


# View All Expenses
def view_all():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

        if not expenses:
            print("No expenses found.")
            return

        print("\nAll Expenses:")
        for expense in expenses:
            print(f"{expense['category']} - ₹{expense['amount']}")

    except:
        print("No expenses found.")


# Get Summary
def get_summary():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

        summary = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            summary[category] = summary.get(category, 0) + amount

        print("\nExpense Summary:")
        for category, total in summary.items():
            print(f"{category}: ₹{total}")

    except:
        print("No expenses found.")


# Menu Loop
while True:
    print("\n----- Expense Tracker -----")
    print("1. Add Expense")
    print("2. Summary")
    print("3. View All")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        add_expense(category, amount)

    elif choice == "2":
        get_summary()

    elif choice == "3":
        view_all()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")