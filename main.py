from flask import Flask, request, jsonify
import re
from urllib.parse import unquote

app = Flask(__name__)

#Valida se o valor segue a máscara e o formato do CNPJ
def is_valid_cnpj(value):
    cnpj_pattern = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
    return re.match(cnpj_pattern, value) is not None

#Endpoint para chamada externa
@app.route('/validate-cnpj', methods=['GET'])
def validate_cnpj():
    
    # Captura os parâmetros da URL
    key = request.args.get('key')
    value = request.args.get('value')
    ctype = request.args.get('type', 'COMPANY')  # Valor padrão COMPANY

    # Decodificar o valor para lidar com codificação dupla
    if value:
        value = unquote(value)

    # Valida se o valor do CNPJ segue a máscara correta
    if not value or not is_valid_cnpj(value):
        return jsonify({
            "success": False,
            "message": "Invalid CNPJ format. Expected format: XX.XXX.XXX/XXXX-XX"
        }), 400

    return jsonify({
        "success": "SUCCESS",
        "message": "CNPJ is valid.",
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
