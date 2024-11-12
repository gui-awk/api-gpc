from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    data = request.json

    if 'base64_pdf' not in data:
        return jsonify({"error": "No base64_pdf field provided"}), 400

    # Decodifica o PDF de Base64 para binário
    try:
        pdf_data = base64.b64decode(data['base64_pdf'])
        # Aqui você pode salvar o PDF, processá-lo, etc.
        # Exemplo: salvando o arquivo localmente
        with open("arquivo_recebido.pdf", "wb") as f:
            f.write(pdf_data)

        return jsonify({"message": "PDF processed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
