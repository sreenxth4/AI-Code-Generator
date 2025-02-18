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

@app.route('/generate', methods=['POST'])  # Ensure it accepts POST requests
def generate_code():
    data = request.get_json()  # Ensure JSON data is parsed correctly
    if not data or "prompt" not in data:
        return jsonify({"error": "Missing 'prompt' field in request body"}), 400
    
    user_prompt = data["prompt"]

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI that writes clean and efficient code."},
                {"role": "user", "content": user_prompt}
            ]
        )
        return jsonify({"response": response.choices[0].message.content})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error message

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's port
    app.run(host="0.0.0.0", port=port)
