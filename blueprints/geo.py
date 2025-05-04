from flask import Blueprint

app = Blueprint('geo', __name__)

@app.route('/')
def geo_index():
    return {"message": "Welcome to the Geo API"}

@app.route('/location')
def geo_location():
    return {"location": "Earth"}
