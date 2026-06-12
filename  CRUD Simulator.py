class TaskNotFoundError(Exception):
    pass


class InvalidTaskDataError(Exception):
    pass


tasks: dict[int, dict] = {}
next_id: int = 1


def get_all_tasks() -> list[dict]:
    return list(tasks.values())


def get_task(id: int) -> dict:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")

    return tasks[id]


def create_task(data: dict) -> dict:
    global next_id

    if "title" not in data:
        raise InvalidTaskDataError("Title is required")

    task = {
        "id": next_id,
        "title": data["title"],
        "completed": data.get("completed", False)
    }

    tasks[next_id] = task
    next_id += 1

    return task


def update_task(id: int, data: dict) -> dict:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")

    tasks[id].update(data)

    return tasks[id]


def delete_task(id: int) -> bool:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")

    del tasks[id]
    return True


while True:
    print("\n--- TASK MANAGER ---")
    print("1. Create Task")
    print("2. Get All Tasks")
    print("3. Get Task By ID")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            title = input("Task title: ")

            task = create_task({
                "title": title
            })

            print("Created:", task)

        elif choice == "2":
            print(get_all_tasks())

        elif choice == "3":
            task_id = int(input("Task ID: "))
            print(get_task(task_id))

        elif choice == "4":
            task_id = int(input("Task ID: "))
            new_title = input("New title: ")

            print(
                update_task(
                    task_id,
                    {"title": new_title}
                )
            )

        elif choice == "5":
            task_id = int(input("Task ID: "))

            delete_task(task_id)
            print("Task deleted")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

    except (TaskNotFoundError, InvalidTaskDataError) as e:
        print(e)

    except ValueError:
        print("Please enter a valid number")