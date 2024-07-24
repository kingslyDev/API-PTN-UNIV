from flask import Flask, jsonify
from crawler import get_ptn_list  # Import fungsi get_ptn_list dari file crawler.py

app = Flask(__name__)

try:
    from crawler import get_ptn_list
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")


# Endpoint untuk mendapatkan daftar PTN
@app.route('/api/ptn', methods=['GET'])
def api_ptn():
    ptn_list = get_ptn_list()  # Panggil fungsi get_ptn_list untuk mendapatkan daftar PTN
    return jsonify(ptn_list)

if __name__ == '__main__':
    app.run(debug=True)
