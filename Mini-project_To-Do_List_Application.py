# Mini-project | To-Do list Application

from datetime import datetime

def display_menu():
    """Display the main menu."""
    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(tasks):
    """Add a new task to the to-do list."""
    task = input("Enter the task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return

    # Add task priority
    priority = input("Enter priority (Low, Medium, High): ").strip().capitalize()
    if priority not in ["Low", "Medium", "High"]:
        print("Invalid priority. Defaulting to 'Low'.")
        priority = "Low"

    # Add task due date
    due_date = input("Enter due date (YYYY-MM-DD, optional): ").strip()
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date() if due_date else None
    except ValueError:
        print("Invalid date format. Due date will not be set.")
        due_date = None

    tasks.append({"task": task, "priority": priority, "due_date": due_date, "completed": False})
    print(f"Task '{task}' added with priority '{priority}' and due date '{due_date}'.")

def view_tasks(tasks):
    """Display all tasks in the to-do list."""
    if not tasks:
        print("Your task list is empty.")
        return

    print("\nYour Tasks:")
    for index, task_info in enumerate(tasks, start=1):
        task = task_info['task']
        priority = task_info['priority']
        due_date = task_info['due_date']
        completed = task_info['completed']
        status = "(X)" if completed else ""
        due_date_str = f" (Due: {due_date})" if due_date else ""
        color = {"Low": "\033[94m", "Medium": "\033[93m", "High": "\033[91m"}.get(priority, "\033[0m")
        print(f"{index}. {color}{task} {status} [Priority: {priority}]{due_date_str}\033[0m")

def mark_task_complete(tasks):
    """Mark a task as complete."""
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the number of the task to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task from the to-do list."""
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['task']}' deleted from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_complete(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Please select a valid option.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    main()

