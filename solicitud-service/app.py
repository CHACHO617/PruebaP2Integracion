from flask import Flask, request, jsonify
import requests
import jwt

app = Flask(__name__)
AUTH_URL = 'http://auth-service:5001/verify'
SOAP_URL = 'http://certificacion-service:5002/registrar'

@app.route('/solicitudes', methods=['POST'])
def crear_solicitud():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    
    # Validar JWT
    auth_response = requests.post(AUTH_URL, headers={"Authorization": f"Bearer {token}"})
    if auth_response.status_code != 200:
        return jsonify({"error": "Token inválido"}), 401

    # Llamada al mock SOAP
    try:
        response = requests.post(SOAP_URL, json={"data": "certificacion"})
        estado = 'procesado' if response.status_code == 200 else 'en revisión'
    except Exception as e:
        return jsonify({"estado": "rechazado", "error": str(e)}), 500

    return jsonify({"estado": estado}), 200

@app.route('/solicitudes/<id>', methods=['GET'])
def obtener_solicitud(id):
    return jsonify({"id": id, "estado": "procesado"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
