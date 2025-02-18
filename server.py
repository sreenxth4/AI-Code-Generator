import openai
from flask import Flask, request, jsonify
import os

# Use environment variables for sensitive information like API keys
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set this in your environment

# Initialize Flask app
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_code():
    data = request.json
    user_prompt = data.get("prompt")

    # Call OpenAI API to generate code
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that writes clean and efficient code."},
            {"role": "user", "content": user_prompt}
        ]
    )

    # Return the generated code
    return jsonify({"code": response['choices'][0]['message']['content']})

# Run the Flask app
if __name__ == '__main__':
port = int(os.environ.get("PORT", 5000))  # Fallback to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)  
