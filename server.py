from sha_256.app import perform_sha256
from flask import Flask, render_template, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash', methods=['POST'])
def hash_string():
    string_to_hash = request.get_json().get("string_to_hash")
    hashed = perform_sha256(string_to_hash)
    expected = hashlib.sha256(string_to_hash.encode('utf-8')).hexdigest()
    return jsonify(hashed = hashed, expected = expected)

#launch server
if __name__ == '__main__':
    app.run(debug=True)
