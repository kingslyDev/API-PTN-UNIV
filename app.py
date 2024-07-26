from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Aktifkan CORS untuk seluruh aplikasi

# Baca data dari file JSON dengan encoding latin-1
with open('ptn_data.json', 'r', encoding='latin-1') as f:
    ptn_data = json.load(f)

@app.route('/ptns', methods=['GET'])
def get_ptns():
    return jsonify(ptn_data)

@app.route('/ptns/<ptn_id>', methods=['GET'])
def get_prodi_by_ptn(ptn_id):
    for ptn in ptn_data:
        if ptn['ptn_id'] == ptn_id:
            return jsonify(ptn)
    return jsonify({'error': 'PTN tidak ditemukan'}), 404

if __name__ == '__main__':
    app.run(debug=True)
