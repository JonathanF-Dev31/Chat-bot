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
