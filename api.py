"""
This script creates a Flask web application that provides a chatbot API for answering questions about specific motorcycle models.
Modules:
    flask: A micro web framework for Python.
    g4f: A module for interacting with the g4f API.
Constants:
    ALLOWED_MODELS (set): A set of allowed motorcycle models.
Routes:
    / (GET): Renders the index.html template.
    /api/chat (POST): Accepts a JSON payload with a motorcycle model and a question, and returns a response from the g4f API.
Functions:
    index(): Renders the index.html template.
    chat(): Handles the chat API endpoint, validates the input, and returns a response from the g4f API.
Usage:
    Run this script to start the Flask web application. The application will be available at http://127.0.0.1:5000/ by default.

"""
from flask import Flask, request, jsonify, render_template
import g4f

app = Flask(__name__)

# Allowed motorcycle models
ALLOWED_MODELS = {"Pulsar N160", "Pulsar NS200", "Pulsar 220F", "Pulsar RS200"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    model = data.get("model", "")
    question = data.get("question", "")

    if model not in ALLOWED_MODELS:
        return jsonify({"response": "⚠️ Invalid model. Please select a valid Pulsar model."})

    if not question:
        return jsonify({"response": "⚠️ Please enter a question."})

    try:
        response_text = g4f.ChatCompletion.create(
            model=g4f.models.default,  # Use the best available free model
            messages=[
                {"role": "system", "content": f"Answer questions about the Pulsar {model} motorcycle."},
                {"role": "user", "content": question}
            ]
        )
        return jsonify({"response": response_text})
    except Exception as e:
        print(f"Error in g4f API: {e}")
        return jsonify({"response": "❌ Error retrieving the response."})

if __name__ == '__main__':
    app.run(debug=True)
