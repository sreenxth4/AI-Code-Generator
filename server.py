import openai
from flask import Flask, request, jsonify
import os

# Use environment variables for sensitive information like API keys
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set this in your environment

# Initialize Flask app
app = Flask(__name__)

# Route for the root URL
@app.route('/')
def home():
    return "Welcome to the Code Generator API!"

@app.route('/generate', methods=['POST'])
def generate_code():
    data = request.json
    user_prompt = data.get("prompt")

    # Call the OpenAI API to generate code based on the prompt
    response = openai.Completion.create(
        model="gpt-4",  # Specify the GPT-4 model
        prompt=user_prompt,  # The prompt provided by the user
        max_tokens=500,  # You can adjust this value based on the response length needed
        temperature=0.7  # You can tweak the temperature to adjust creativity
    )

    # Return the generated code as a JSON response
    return jsonify({"generated_code": response.choices[0].text.strip()})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Fallback to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
