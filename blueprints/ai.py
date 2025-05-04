from flask import Blueprint, request

app = Blueprint('ai', __name__)

@app.route('/')
def ai_index():
    return {"message": "Welcome to the AI API"}

@app.route('/potato')
def potato():
    return {"message": "This is an ai potato"}