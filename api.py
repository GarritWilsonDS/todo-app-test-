from flask import Flask, jsonify, request
from database import Database

app = Flask(__name__)
db = Database(db_name="todo.db")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Endpoint to get all tasks"""
    try:
        tasks = db.show_tasks()
        return jsonify({"tasks": tasks, "status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500

@app.route("/tasks", methods=["POST"])
def add_task():
    """Endpoint to add a new task"""
    try:
        task = request.json.get("task")
        if not task:
            return jsonify({"error": "No task provided", "status": "error"}), 400
        
        db.add_task(task)
        return jsonify({"message": "Task added successfully", "status": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500

@app.route("/tasks/<task>", methods=["DELETE"])
def delete_task(task):
    """Endpoint to delete a specific task"""
    try:
        db.remove_task(task)
        return jsonify({"message": "Task deleted successfully", "status": "success"}), 200
    except ValueError:
        return jsonify({"error": "Task not found", "status": "error"}), 404
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500

@app.route("/tasks", methods=["DELETE"])
def clear_tasks():
    """Endpoint to clear all tasks"""
    try:
        db.clear_tasks()
        return jsonify({"message": "All tasks cleared successfully", "status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500

@app.teardown_appcontext
def cleanup(exception=None):
    """Ensure database connection is closed when the application context ends"""
    db.close()

if __name__ == "__main__":
    app.run(debug=True)