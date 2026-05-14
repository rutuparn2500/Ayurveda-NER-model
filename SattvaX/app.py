from flask import Flask, render_template, request, jsonify
import os
from nlp_pipeline import analyze_text
from evaluation import get_evaluation_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/evaluation')
def evaluation_api():
    data = get_evaluation_data()
    return jsonify(data)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text_input', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
        
    result = analyze_text(text)
    
    return jsonify({
        'status': 'success',
        **result
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)
