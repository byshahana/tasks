contacts = {}

while True:
    choice = input("\nadd/search/update/delete/list/exit: ")

    if choice == "exit":
        break

    elif choice == "add":
        name = input("Name: ")
        contacts[name] = input("Phone: ")
        print(f"{name} added")

    elif choice == "search":
        name = input("Name: ")
        print(f"{name}: {contacts.get(name, 'Not found')}")

    elif choice == "update":
        name = input("Name: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
            print(f"{name} updated")
        else:
            print(f"{name} not found")

    elif choice == "delete":
        name = input("Name: ")
        if contacts.pop(name, None):
            print(f"{name} deleted")
        else:
            print(f"{name} not found")

    elif choice == "list":
        for n in sorted(contacts):
            print(f"{n}: {contacts[n]}")    