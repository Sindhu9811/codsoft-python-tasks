import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== TO-DO LIST ==========")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(
            f'{task["id"]}. {task["title"]} - {status}'
        )

    print("================================")


def add_task(tasks):
    """Add a new task."""
    title = input("\nEnter the task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    new_id = max([task["id"] for task in tasks], default=0) + 1

    task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def complete_task(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to mark as completed: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)

            print("Task marked as completed!")
            return

    print("Task not found.")


def update_task(tasks):
    """Update an existing task."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to update: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter the new task description: ").strip()

            if not new_title:
                print("Task description cannot be empty.")
                return

            task["title"] = new_title
            save_tasks(tasks)

            print("Task updated successfully!")
            return

    print("Task not found.")


def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)

            print("Task deleted successfully!")
            return

    print("Task not found.")


def main():
    """Main program."""
    tasks = load_tasks()

    while True:
        print("\n")
        print("========== TO-DO LIST APPLICATION ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        print("============================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            update_task(tasks)

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            print("\nThank you for using the To-Do List Application!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
