from flask import Flask, send_from_directory, request
import os
from blueprints.ai import app as ai_app
from blueprints.geo import app as geo_app
from blueprints.users import app as users_app

app = Flask(__name__, static_folder='static', static_url_path='/static')

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

# Register the AI blueprint
app.register_blueprint(ai_app, url_prefix='/ai')

# Register the Geo blueprint
app.register_blueprint(geo_app, url_prefix='/geo')

# Register the Users blueprint
app.register_blueprint(users_app, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
