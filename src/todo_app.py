#!/usr/bin/env python3
"""
Console Todo Application - Phase I

A simple in-memory todo list application with CLI interface.
"""

# Import required modules
import datetime
from typing import List, Optional


class Task:
    """Represents a single todo item."""

    def __init__(self, task_id: int, description: str, completed: bool = False):
        self.id = task_id
        self.description = description
        self.completed = completed
        self.created_at = datetime.datetime.now()


class TodoList:
    """Manages a collection of tasks in memory."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description: str) -> Optional[Task]:
        """Add a new task to the list."""
        if not description.strip():
            return None
        task = Task(self.next_id, description.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks."""
        return self.tasks

    def update_task(self, task_id: int, new_description: str) -> bool:
        """Update a task's description."""
        task = self.get_task(task_id)
        if task and new_description.strip():
            task.description = new_description.strip()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_complete(self, task_id: int) -> bool:
        """Mark a task as complete."""
        task = self.get_task(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete."""
        task = self.get_task(task_id)
        if task:
            task.completed = False
            return True
        return False

    def get_tasks_by_status(self, completed: bool) -> List[Task]:
        """Get tasks by completion status."""
        return [task for task in self.tasks if task.completed == completed]


def display_menu():
    """Display the main menu."""
    print("\nTodo List Application")
    print("====================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")
    print()


def get_user_choice():
    """Get and validate user's menu choice."""
    try:
        choice = input("Enter your choice (1-7): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            return None
    except KeyboardInterrupt:
        print("\n\nExiting application...")
        return '7'
    except EOFError:
        print("\n\nExiting application...")
        return '7'


def main():
    """Main application entry point with menu loop."""
    todo_list = TodoList()

    print("Welcome to the Todo List Application!")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice is None:
            continue  # Invalid choice, show menu again

        if choice == '1':
            description = input("Enter task description: ").strip()
            task = todo_list.add_task(description)
            if task:
                print(f"Task '{task.description}' added with ID {task.id}")
            else:
                print("Task description cannot be empty.")

        elif choice == '2':
            tasks = todo_list.get_all_tasks()
            if tasks:
                print("\nYour Tasks:")
                for task in tasks:
                    status = "✓" if task.completed else " "
                    print(f"{task.id}. [{status}] {task.description}")
            else:
                print("\nNo tasks in your list.")

        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: ").strip())
                new_description = input("Enter new description: ").strip()

                if todo_list.update_task(task_id, new_description):
                    print(f"Task {task_id} updated successfully.")
                else:
                    print(f"Failed to update task {task_id}. Task may not exist or description is empty.")
            except ValueError:
                print("Invalid task ID. Please enter a number.")

        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: ").strip())

                # Show the task before deletion
                task = todo_list.get_task(task_id)
                if task:
                    print(f"About to delete task: {task.description}")
                    confirm = input("Are you sure? (y/N): ").strip().lower()
                    if confirm in ['y', 'yes']:
                        if todo_list.delete_task(task_id):
                            print(f"Task {task_id} deleted successfully.")
                        else:
                            print(f"Failed to delete task {task_id}.")
                    else:
                        print("Deletion cancelled.")
                else:
                    print(f"Task {task_id} does not exist.")
            except ValueError:
                print("Invalid task ID. Please enter a number.")

        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to mark complete: ").strip())

                if todo_list.mark_complete(task_id):
                    print(f"Task {task_id} marked as complete.")
                else:
                    print(f"Failed to mark task {task_id} as complete. Task may not exist.")
            except ValueError:
                print("Invalid task ID. Please enter a number.")

        elif choice == '6':
            try:
                task_id = int(input("Enter task ID to mark incomplete: ").strip())

                if todo_list.mark_incomplete(task_id):
                    print(f"Task {task_id} marked as incomplete.")
                else:
                    print(f"Failed to mark task {task_id} as incomplete. Task may not exist.")
            except ValueError:
                print("Invalid task ID. Please enter a number.")

        elif choice == '7':
            print("Thank you for using the Todo List Application!")
            break

        else:
            print(f"Option {choice} is not yet implemented.")


if __name__ == "__main__":
    main()