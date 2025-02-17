# Todo List Application

A simple command-line todo list application built with Python, featuring basic task management functionality.

## Features

- Add new tasks
- Remove existing tasks
- Show all tasks
- Clear all tasks
- Command-line interface

## Project Structure

- `todo.py`: Core TodoList class implementation
- `ui.py`: Command-line user interface
- `api.py`: API endpoints (in development)
- `database.py`: Database operations (in development)

## Setup

1. Clone the repository
2. Navigate to the todo app directory
3. Run the application:
```bash
python ui.py
```

## Usage

The application provides a simple menu-driven interface:

1. **Add Task**: Add a new task to the list
2. **Remove Task**: Remove an existing task
3. **Show Tasks**: Display all current tasks
4. **Clear Tasks**: Remove all tasks
5. **Exit**: Close the application

## Example

```bash
1. Add Task
2. Remove Task
3. Show Tasks
4. Clear Tasks
5. Exit
Enter your choice: 1
Enter a task: Buy groceries
```

## Development

- Written in Python
- Uses in-memory list for storage (database integration coming soon)
- Modular design for easy expansion

## Future Enhancements

- Database persistence
- RESTful API
- Web interface
- Task priorities
- Due dates
- Categories/Tags

## License

MIT License 