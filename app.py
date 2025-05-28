from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Permitir CORS desde el frontend
CORS(app, origins=["https://front.hombres.pro"])

# Endpoint de health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify(status='ok'), 200

# Endpoint GET /users
@app.route('/users', methods=['GET'])
def list_users():
    users = [
        {"id": 1, "name": "Carlos Serrano", "email": "carlospro@gmail.com"},
        {"id": 2, "name": "Lena Orozco",  "email": "niger23@gmail.com"}
    ]
    return jsonify(users=users), 200

# Endpoint POST /users
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # Aquí crearías el usuario en tu base de datos...
    nuevo = {"id": 3, **data}
    return jsonify(user=nuevo), 201

# Endpoint PUT /users/<id>
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    # Aquí actualizarías el usuario en tu base de datos...
    updated = {"id": user_id, **data}
    return jsonify(user=updated), 200

# Endpoint DELETE /users/<id>
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Aquí eliminarías el usuario de tu base de datos...
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
