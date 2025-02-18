import requests

BASE_URL = "http://localhost:5000"

def display_menu():
    print("\n=== Todo API Test Menu ===")
    print("1. Add Task")
    print("2. Show All Tasks")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def add_task():
    task = input("Enter task to add: ")
    try:
        response = requests.post(
            f"{BASE_URL}/tasks",
            json={"task": task}
        )
        response.raise_for_status()  # Raise an error for bad status codes
        print("\nResponse:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"\nError making request: {str(e)}")
        print(f"Response content: {response.text}")  # Print raw response

def show_tasks():
    try:
        response = requests.get(f"{BASE_URL}/tasks")
        response.raise_for_status()
        tasks = response.json().get("tasks", [])
        print("\nCurrent Tasks:")
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    except requests.exceptions.RequestException as e:
        print(f"\nError making request: {str(e)}")
        print(f"Response content: {response.text}")

def delete_task():
    task = input("Enter task to delete: ")
    try:
        response = requests.delete(f"{BASE_URL}/tasks/{task}")
        response.raise_for_status()
        print("\nResponse:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"\nError making request: {str(e)}")
        print(f"Response content: {response.text}")

def clear_tasks():
    confirm = input("Are you sure you want to clear all tasks? (y/n): ")
    if confirm.lower() == 'y':
        try:
            response = requests.delete(f"{BASE_URL}/tasks")
            response.raise_for_status()
            print("\nResponse:", response.json())
        except requests.exceptions.RequestException as e:
            print(f"\nError making request: {str(e)}")
            print(f"Response content: {response.text}")
    else:
        print("\nOperation cancelled.")

def test_api():
    while True:
        choice = display_menu()
        
        try:
            if choice == "1":
                add_task()
            elif choice == "2":
                show_tasks()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                clear_tasks()
            elif choice == "5":
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
        except requests.exceptions.ConnectionError:
            print("\nError: Cannot connect to the API. Is the server running?")
            print("Make sure to run 'python api.py' in a separate terminal")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    print("Testing Todo API...")
    print(f"Connecting to: {BASE_URL}")
    test_api() 