tasks = []

def display_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nTo-Do List")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("\nEnter task: ").strip()

    if title:
        tasks.append({"title": title, "completed": False})
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

def update_task():
    display_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to update: "))

        if 1 <= number <= len(tasks):
            new_title = input("Enter new task: ").strip()

            if new_title:
                tasks[number - 1]["title"] = new_title
                print("Task updated successfully.")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def complete_task():
    display_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to mark as completed: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    display_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Thank you for using the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
