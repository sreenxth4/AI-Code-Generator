import openai
from flask import Flask, request, jsonify
import os

# Use environment variables for sensitive information like API keys
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure this is set in your environment

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Code Generator API!"

@app.route('/generate', methods=['POST'])
def generate_code():
    try:
        data = request.json
        if not data or "prompt" not in data:
            return jsonify({"error": "Missing 'prompt' in request"}), 400  # Bad Request
        
        user_prompt = data["prompt"]

        # Call the OpenAI API to generate code
        response = openai.Completion.create(
            model="gpt-4",
            prompt=user_prompt,
            max_tokens=500,
            temperature=0.7
        )

        return jsonify({"generated_code": response.choices[0].text.strip()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error details

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)  # Enable debug mode
