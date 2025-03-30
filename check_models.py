import google.generativeai as genai

genai.configure(api_key="AIzaSyDmZTkvMv4A5412g-Mw-NAnCIdoiJEjkr8")

# List available models
models = genai.list_models()
for model in models:
    print(model.name)
