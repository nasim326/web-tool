import os
from flask import Flask, request, send_file, jsonify
from processor import process_files

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "Backend is running. Please access the frontend."

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        files = ['shipper_list', 'spool_status', 'spool_joint_data']
        for file in files:
            if file not in request.files:
                return jsonify({"error": f"Missing {file} file"}), 400
            request.files[file].save(os.path.join(UPLOAD_FOLDER, file + '.xlsx'))

        output_path = process_files()
        return jsonify({"message": "Files processed successfully", "download_url": "/download"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download', methods=['GET'])
def download_file():
    try:
        return send_file('uploads/master_file.xlsx', as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
