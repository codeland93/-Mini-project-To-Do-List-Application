# To-Do List Application
Overview:
The To-Do List CLI Application is a simple command-line interface (CLI) tool that helps users manage their tasks. It allows users to add, view, mark as complete, and delete tasks. Additionally, tasks can be assigned priorities and due dates, with color-coding for easy identification.

Features:
Add a Task: Users can add a new task with an optional priority and due date.

View Tasks: Displays all tasks, including their priority, due date, and completion status.

Mark a Task as Complete: Allows users to mark a task as complete.

Delete a Task: Users can delete a task from the list.

Quit: Exits the application.

Priority and Due Date Features

Task Priorities: Tasks can have priorities of "Low," "Medium," or "High." These are displayed in different colors:

Low: Blue
Medium: Yellow
High: Red

Due Dates: Tasks can have an optional due date in the format YYYY-MM-DD. If provided, this date is displayed alongside the task.

How to Use:
Run the application in your terminal.

Menu Options:
Upon running the application, a menu is displayed with the following options:

Welcome to the To-Do List App!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit

Select an option by entering the corresponding number and pressing Enter.

Adding a Task:
Enter the task description.
Optionally, enter a priority (Low, Medium, High). If not specified or invalid, the default priority is "Low."
Optionally, enter a due date in YYYY-MM-DD format. If the format is incorrect, the due date will not be set.

Viewing Tasks:
All tasks are displayed with their description, priority, due date, and completion status.

Marking a Task as Complete:
View the list of tasks.
Enter the number of the task you wish to mark as complete. The task will be marked with "(X)."

Deleting a Task:
View the list of tasks.
Enter the number of the task you wish to delete. The task will be removed from the list.

Quitting the Application:
Select the "Quit" option from the menu to exit the application.

Code Organization:
Functions:
display_menu(): Displays the main menu.
add_task(tasks): Adds a new task to the list.
view_tasks(tasks): Displays all tasks.
mark_task_complete(tasks): Marks a selected task as complete.
delete_task(tasks): Deletes a selected task.
main(): The main function that runs the application loop.

Error Handling:
The application handles invalid user inputs gracefully, providing appropriate feedback and defaulting to safe values where applicable.
Date parsing is handled with the datetime module, and invalid date formats are caught and handled.

Optional Features:
Task priorities, due dates, and color-coding enhance the functionality of the application, making it easier to manage and prioritize tasks.

Thank you reading and using the application. :)

