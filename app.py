from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        text = data.get('text', '').strip()
        target_language = data.get('language', '').strip()

        if not text:
            return jsonify({'error': 'Please enter text for translation.'})
        if not target_language:
            return jsonify({'error': 'Please select a target language.'})

        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        if not translated_text:
            return jsonify({'error': 'Translation failed. Please try again later.'})

        return jsonify({'translated_text': translated_text})

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'})

if __name__ == '__main__':
    app.run(debug=True)
