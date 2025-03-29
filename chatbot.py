from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Correct placement of CORS

# Configure Gemini API
API_KEY = "AIzaSyDmZTkvMv4A5412g-Mw-NAnCIdoiJEjkr8"  # Replace with your valid API key
genai.configure(api_key=API_KEY)

# Chat function
def chat_with_ai(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Use available model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")
        if not user_input:
            return jsonify({"error": "Message cannot be empty"}), 400

        ai_response = chat_with_ai(user_input)
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
