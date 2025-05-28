from flask import Flask, jsonify, request

app = Flask(__name__)

# Ejemplo de endpoint GET
@app.route('/api/items', methods=['GET'])
def get_items():
    items = [
        {"id": 1, "name": "Manzana"},
        {"id": 2, "name": "Banana"}
    ]
    return jsonify(items=items), 200

# Ejemplo de endpoint POST
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    # Aquí crearías el ítem en tu base de datos...
    nuevo = {"id": 3, **data}
    return jsonify(item=nuevo), 201

if __name__ == '__main__':
    # Solo para desarrollo local: flask run
    app.run(host='0.0.0.0', port=5000, debug=True)

