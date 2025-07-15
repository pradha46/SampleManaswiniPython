# app.py (Flask example)
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [] # In-memory list for demonstration
next_id = 1

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    global next_id
    data = request.json
    new_todo = {'id': next_id, 'title': data['title'], 'completed': False}
    todos.append(new_todo)
    next_id += 1
    return jsonify(new_todo), 201

# ... (Implement PUT, DELETE, GET by ID similarly)

if __name__ == '__main__':
    app.run(debug=True)
