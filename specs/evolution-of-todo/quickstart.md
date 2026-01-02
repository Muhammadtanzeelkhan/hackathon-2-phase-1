# Quickstart Guide: Console Todo Application - Phase I

**Created**: 2026-01-02
**Feature**: Console Todo Application - Phase I

## Getting Started

### Prerequisites

- Python 3.11 or higher installed on your system
- Console/terminal access

### Running the Application

1. Ensure you have Python installed:
   ```bash
   python --version
   ```

2. Run the application:
   ```bash
   python src/todo_app.py
   ```

3. The application will display a menu with options for managing your todo tasks.

## Using the Application

### Main Menu

When the application starts, you'll see a menu with the following options:

```
Todo List Application
====================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
```

### Adding a Task

1. Select option 1 from the menu
2. Enter your task description when prompted
3. The task will be added to your list with a unique ID

### Viewing Tasks

1. Select option 2 from the menu
2. All tasks will be displayed with their ID, description, and completion status
3. Completed tasks will be marked with [✓] and incomplete tasks with [ ]

### Updating a Task

1. Select option 3 from the menu
2. Enter the ID of the task you want to update
3. Enter the new description for the task
4. The task description will be updated

### Deleting a Task

1. Select option 4 from the menu
2. Enter the ID of the task you want to delete
3. The task will be removed from your list

### Marking a Task Complete

1. Select option 5 from the menu
2. Enter the ID of the task you want to mark as complete
3. The task status will be updated to complete

### Marking a Task Incomplete

1. Select option 6 from the menu
2. Enter the ID of the task you want to mark as incomplete
3. The task status will be updated to incomplete

### Exiting the Application

1. Select option 7 from the menu
2. The application will exit

## Error Handling

- If you enter an invalid task ID, you'll receive an error message
- If you try to perform an operation on a non-existent task, you'll receive an error message
- If you enter an invalid menu option, you'll be prompted to try again

## Important Notes

- All data is stored in memory only and will be lost when the application exits
- The application supports single-user operation only
- Task IDs are automatically assigned and cannot be changed