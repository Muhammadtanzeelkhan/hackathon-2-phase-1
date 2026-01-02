"""
Unit tests for the Console Todo Application - Phase I
"""

import pytest
from src.todo_app import Task, TodoList


def test_task_creation():
    """Test that a task can be created with required attributes."""
    task = Task(1, "Test task")
    assert task.id == 1
    assert task.description == "Test task"
    assert task.completed is False
    assert task.created_at is not None


def test_todo_list_initialization():
    """Test that TodoList is initialized with empty tasks and ID counter."""
    todo_list = TodoList()
    assert len(todo_list.tasks) == 0
    assert todo_list.next_id == 1


def test_add_task():
    """Test adding a task to the todo list."""
    todo_list = TodoList()
    task = todo_list.add_task("Test task")

    assert len(todo_list.tasks) == 1
    assert task.id == 1
    assert task.description == "Test task"


def test_get_task():
    """Test retrieving a task by ID."""
    todo_list = TodoList()
    added_task = todo_list.add_task("Test task")

    retrieved_task = todo_list.get_task(1)
    assert retrieved_task is not None
    assert retrieved_task.id == 1
    assert retrieved_task.description == "Test task"


def test_get_nonexistent_task():
    """Test retrieving a task that doesn't exist."""
    todo_list = TodoList()
    retrieved_task = todo_list.get_task(999)
    assert retrieved_task is None


def test_get_all_tasks():
    """Test retrieving all tasks."""
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")

    all_tasks = todo_list.get_all_tasks()
    assert len(all_tasks) == 2


def test_add_task_functionality():
    """Test the add_task functionality."""
    todo_list = TodoList()
    task = todo_list.add_task("New task")

    assert task.id == 1
    assert task.description == "New task"
    assert task.completed is False
    assert len(todo_list.tasks) == 1


def test_task_validation():
    """Test task description validation."""
    todo_list = TodoList()

    # Test that empty description is not allowed
    task = todo_list.add_task("")
    assert task is None

    # Test that whitespace-only description is not allowed
    task = todo_list.add_task("   ")
    assert task is None

    # Test that valid description is allowed
    task = todo_list.add_task("Valid task")
    assert task is not None
    assert task.description == "Valid task"


def test_view_all_tasks():
    """Test viewing all tasks functionality."""
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    todo_list.add_task("Task 3")

    all_tasks = todo_list.get_all_tasks()
    assert len(all_tasks) == 3

    # Check that tasks are returned in the order they were added
    assert all_tasks[0].description == "Task 1"
    assert all_tasks[1].description == "Task 2"
    assert all_tasks[2].description == "Task 3"


def test_empty_list_handling():
    """Test handling of empty task list."""
    todo_list = TodoList()
    all_tasks = todo_list.get_all_tasks()
    assert len(all_tasks) == 0


def test_update_task_descriptions():
    """Test updating task descriptions functionality."""
    todo_list = TodoList()
    task = todo_list.add_task("Original task")

    # Verify initial state
    assert task.description == "Original task"

    # Update the task
    success = todo_list.update_task(task.id, "Updated task")
    assert success is True

    # Verify the update
    updated_task = todo_list.get_task(task.id)
    assert updated_task.description == "Updated task"


def test_update_invalid_task_id():
    """Test updating a task with invalid ID."""
    todo_list = TodoList()

    # Try to update a task that doesn't exist
    success = todo_list.update_task(999, "New description")
    assert success is False


def test_update_with_empty_description():
    """Test updating a task with empty description."""
    todo_list = TodoList()
    task = todo_list.add_task("Original task")

    # Try to update with empty description
    success = todo_list.update_task(task.id, "")
    assert success is False

    # Try to update with whitespace-only description
    success = todo_list.update_task(task.id, "   ")
    assert success is False

    # Verify the original description remains unchanged
    unchanged_task = todo_list.get_task(task.id)
    assert unchanged_task.description == "Original task"


def test_delete_task_functionality():
    """Test deleting tasks functionality."""
    todo_list = TodoList()
    task1 = todo_list.add_task("Task 1")
    task2 = todo_list.add_task("Task 2")
    task3 = todo_list.add_task("Task 3")

    # Verify initial state
    assert len(todo_list.tasks) == 3

    # Delete the middle task
    success = todo_list.delete_task(task2.id)
    assert success is True
    assert len(todo_list.tasks) == 2

    # Verify the deleted task is gone
    deleted_task = todo_list.get_task(task2.id)
    assert deleted_task is None

    # Verify other tasks still exist
    remaining_task1 = todo_list.get_task(task1.id)
    remaining_task3 = todo_list.get_task(task3.id)
    assert remaining_task1 is not None
    assert remaining_task3 is not None


def test_delete_invalid_task_id():
    """Test deleting a task with invalid ID."""
    todo_list = TodoList()
    todo_list.add_task("Task 1")

    # Try to delete a task that doesn't exist
    success = todo_list.delete_task(999)
    assert success is False

    # Verify the list remains unchanged
    assert len(todo_list.tasks) == 1


def test_mark_task_complete():
    """Test marking tasks as complete functionality."""
    todo_list = TodoList()
    task = todo_list.add_task("Incomplete task")

    # Verify initial state
    assert task.completed is False

    # Mark as complete
    success = todo_list.mark_complete(task.id)
    assert success is True

    # Verify the update
    updated_task = todo_list.get_task(task.id)
    assert updated_task.completed is True


def test_mark_task_incomplete():
    """Test marking tasks as incomplete functionality."""
    todo_list = TodoList()
    task = todo_list.add_task("Complete task")

    # First mark as complete
    todo_list.mark_complete(task.id)
    assert task.completed is True

    # Mark as incomplete
    success = todo_list.mark_incomplete(task.id)
    assert success is True

    # Verify the update
    updated_task = todo_list.get_task(task.id)
    assert updated_task.completed is False


def test_mark_invalid_task_id():
    """Test marking tasks with invalid ID."""
    todo_list = TodoList()
    todo_list.add_task("Task 1")

    # Try to mark complete a task that doesn't exist
    success_complete = todo_list.mark_complete(999)
    assert success_complete is False

    # Try to mark incomplete a task that doesn't exist
    success_incomplete = todo_list.mark_incomplete(999)
    assert success_incomplete is False