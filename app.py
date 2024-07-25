from flask import Flask, jsonify, request
from flask_cors import CORS
from crawler import get_ptn_list, get_prodi_list

app = Flask(__name__)
CORS(app)  # Aktifkan CORS untuk seluruh aplikasi

@app.route('/api/ptn', methods=['GET'])
def api_ptn():
    ptn_list = get_ptn_list()
    return jsonify(ptn_list)

@app.route('/api/prodi', methods=['GET'])
def api_prodi():
    ptn_id = request.args.get('id')
    if not ptn_id:
        return jsonify({'error': 'Missing "id" parameter'}), 400

    prodi_list = get_prodi_list(ptn_id)
    return jsonify(prodi_list)

if __name__ == '__main__':
    app.run(debug=True)
