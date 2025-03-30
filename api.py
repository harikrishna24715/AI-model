import google.generativeai as genai

# Set up API key
genai.configure(api_key="AIzaSyDmZTkvMv4A5412g-Mw-NAnCIdoiJEjkr8")

# Create a function to interact with the model
def chat_with_ai(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Example Usage
user_input = "Tell me a joke!"
print(chat_with_ai(user_input))
