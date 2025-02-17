from todo import TodoList

def main():
    todo_list = TodoList()

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Clear Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter a task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            print(todo_list.show_tasks())
        elif choice == "4":
            todo_list.clear_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()