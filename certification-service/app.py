from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/registrar', methods=['POST'])
def registrar_certificacion():
    return jsonify({"mensaje": "Certificación registrada con éxito"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
