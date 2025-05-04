from flask import Blueprint

app = Blueprint('users', __name__)

@app.route('/')
def users_index():
    return {"message": "Welcome to the Users API"}

@app.route('/profile')
def users_profile():
    return {"profile": "User Profile Data"}
