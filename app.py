from flask import Flask, request, render_template
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the model without custom objects
model = load_model('C:/MLfinal/my_flask_app/model/cat_dog_classifier.keras')

@app.route('/')
def index():
    return render_template('index.html')

# Add other routes as necessary
