import openai
from flask import Flask, request, jsonify
import os

# Ensure the OpenAI API key is set
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Code Generator API!"

@app.route('/generate', methods=['POST'])
def generate_code():
    data = request.json
    user_prompt = data.get("prompt")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that writes clean and efficient code."},
            {"role": "user", "content": user_prompt}
        ]
    )

    return jsonify(response['choices'][0]['message']['content'])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Bind to Render's port
    app.run(host="0.0.0.0", port=port)
