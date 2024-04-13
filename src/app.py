from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
   {"label": "Mi primera tarea", "done":False}
]
@app.route('/todos', methods=['GET'])
def get_todos():
  json_todos = jsonify(todos)
  return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    new_todo = request_body["label"]
    todos.append({"label": new_todo, "done": False})
    json_todos = jsonify(todos)
    return json_todos
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Posición inválida"})
    del todos[position]
    json_todos = jsonify(todos)
    return json_todos
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)