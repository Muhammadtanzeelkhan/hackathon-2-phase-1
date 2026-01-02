# Data Model: Console Todo Application - Phase I

**Created**: 2026-01-02
**Feature**: Console Todo Application - Phase I
**Input**: Feature specification requirements

## Entity: Task

**Description**: Represents a single todo item in the application

### Attributes

- **id** (integer)
  - Unique identifier for the task
  - Auto-generated sequentially starting from 1
  - Required, immutable after creation
  - Validation: Must be positive integer

- **description** (string)
  - Text content of the task
  - Required field
  - Validation: Cannot be empty or whitespace only

- **completed** (boolean)
  - Status indicating whether the task is completed
  - Default value: False
  - Can be toggled between True/False

- **created_at** (datetime)
  - Timestamp when the task was created
  - Automatically set when task is created
  - Read-only after creation

### State Transitions

- **Incomplete → Complete**: When user marks task as complete
- **Complete → Incomplete**: When user marks task as incomplete

### Validation Rules

- ID must be unique within the TodoList
- Description cannot be empty or contain only whitespace
- Completed status can only be True or False

## Entity: TodoList

**Description**: Collection of Task objects with operations for managing tasks

### Attributes

- **tasks** (list of Task objects)
  - Contains all tasks in the list
  - Maintains order of creation

- **next_id** (integer)
  - Tracks the next ID to assign to new tasks
  - Starts at 1 and increments for each new task

### Operations

- **add_task(description)**: Creates and adds a new Task with unique ID
- **get_task(task_id)**: Retrieves a Task by its ID
- **update_task(task_id, new_description)**: Updates a Task's description
- **delete_task(task_id)**: Removes a Task by its ID
- **mark_complete(task_id)**: Sets a Task's status to completed
- **mark_incomplete(task_id)**: Sets a Task's status to incomplete
- **get_all_tasks()**: Returns all tasks
- **get_tasks_by_status(completed)**: Returns tasks with specific completion status

### Validation Rules

- Task ID must exist before performing operations on it
- Description cannot be empty when updating
- Operations fail gracefully with appropriate error messages for invalid inputs