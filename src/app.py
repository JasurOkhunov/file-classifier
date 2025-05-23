from flask import Flask, request, jsonify
from src.classifier import classify_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpeg', 'jpg', 'docx', 'xlsx', 'csv', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/classify_file', methods=['POST'])
def classify_file_route():

    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed"}), 400

    file_class = classify_file(file)
    return jsonify({"file_class": file_class}), 200

@app.route("/", methods=["GET"])
def root():
    return "Service is up", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)