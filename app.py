from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, jsonify, url_for, session
import os
from PIL import Image
import google.generativeai as genai
import io
import base64

app = Flask(__name__, static_folder='static')
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this-in-production')

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load the gemma model
model = genai.GenerativeModel("models/gemma-3-27b-it")

def get_gemma_response(input_text, image, prompt):
    response = model.generate_content([prompt, image])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        return image
    else:
        raise FileNotFoundError("No image uploaded")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/save-api-key', methods=['POST'])
def save_api_key():
    try:
        data = request.get_json()
        api_key = data.get('api_key')
        
        if not api_key:
            return jsonify({'error': 'No API key provided'}), 400
        
        # Store API key in session
        session['google_api_key'] = api_key
        
        return jsonify({'message': 'API key saved successfully'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/test-api-key', methods=['POST'])
def test_api_key():
    try:
        data = request.get_json()
        api_key = data.get('api_key')
        
        if not api_key:
            return jsonify({'error': 'No API key provided'}), 400
        
        # Test the API key by creating a simple request
        genai.configure(api_key=api_key)
        
        # Try to create a model instance to test the key
        test_model = genai.GenerativeModel("models/gemma-3-27b-it")
        
        return jsonify({'message': 'API key is valid and working'})
        
    except Exception as e:
        return jsonify({'error': f'API key test failed: {str(e)}'}), 400

@app.route('/analyze', methods=['POST'])
def analyze_invoice():
    try:
        # Get the uploaded file and model selection
        uploaded_file = request.files['image']
        input_text = request.form.get('input_text', '')
        selected_model = request.form.get('model', 'models/gemma-3-27b-it')
        
        if not uploaded_file:
            return jsonify({'error': 'No image uploaded'}), 400
        
        # Get API key from session or environment
        api_key = session.get('google_api_key') or os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            return jsonify({'error': 'No API key configured. Please go to Settings to add your Google API key.'}), 400
        
        # Configure genai with the API key
        genai.configure(api_key=api_key)
        
        # Create model instance with selected model
        model = genai.GenerativeModel(selected_model)
        
        # Process the image
        image_data = input_image_setup(uploaded_file)
        
        # Define the prompt
        input_prompt = """
        you are an expert in understanding invoices. We will upload an image as invoice
        and you will have to answer any questions based on the uploaded invoice image
        """
        
        # Get response from the model
        response = model.generate_content([input_prompt, image_data])
        
        return jsonify({'response': response.text})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
