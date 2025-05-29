from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET = 'clave-secreta'

@app.route('/verify', methods=['POST'])
def verify_token():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        return jsonify({"user": payload["user"], "role": payload["role"]}), 200
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token inválido"}), 401

@app.route('/token', methods=['POST'])
def generar_token():
    datos = request.get_json()
    user = datos.get("user", "usuario")
    role = datos.get("role", "estudiante")

    token = jwt.encode({"user": user, "role": role}, SECRET, algorithm="HS256")
    return jsonify({"token": token})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
