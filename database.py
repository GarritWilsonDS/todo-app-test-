import sqlite3

class Database:
    def __init__(self, db_name:"todo.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)")
        self.conn.commit()

    def add_task(self, task):
        self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        self.conn.commit()

    def remove_task(self, task):
        self.cursor.execute("DELETE FROM tasks WHERE task = ?", (task,))
        self.conn.commit()

    def show_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()
    
    def clear_tasks(self):
        self.cursor.execute("DELETE FROM tasks")
        self.conn.commit()

    def close(self):
        self.conn.close()   