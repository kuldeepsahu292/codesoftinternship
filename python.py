1# Initialize an empty list to store tasks
tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def mark_completed():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            print(f"Task '{completed_task}' marked as completed.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
