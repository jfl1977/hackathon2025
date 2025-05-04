from flask import Flask, send_from_directory, request
import os

app = Flask(__name__, static_folder='public', static_url_path='/static')

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/potato')
def potato():
    return {"message": "This is a potato"}

@app.route('/upload-form')
def upload_form():
    return send_from_directory(app.static_folder, 'upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return {"error": "No file part"}, 400
    file = request.files['file']
    if file.filename == '':
        return {"error": "No selected file"}, 400
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return {"message": "File uploaded successfully"}

if __name__ == '__main__':
    app.run(debug=True)
