from database import Database

class TodoList:
    def __init__(self):
        self.db = Database(db_name="todo.db")

    def add_task(self, task):
        self.db.add_task(task)

    def remove_task(self, task):
        self.db.remove_task(task)

    def show_tasks(self):
        return self.db.show_tasks()
    
    def clear_tasks(self):
        self.db.clear_tasks()

    def close(self):
        self.db.close() 