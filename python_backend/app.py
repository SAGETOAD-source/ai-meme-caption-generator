from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from caption_generator import generate_meme_caption

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "AI Meme Generator"})

@app.route('/api/generate', methods=['POST'])
def generate_caption():
    data = request.json
    template_id = data.get('template_id')
    topic = data.get('topic')
    keywords = data.get('keywords', [])
    
    if not template_id:
        return jsonify({"error": "Template ID is required"}), 400
        
    try:
        # Generate caption using NLP model
        caption = generate_meme_caption(template_id, topic, keywords)
        return jsonify({
            "success": True, 
            "caption": caption,
            "template_id": template_id
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # In a real scenario, we would classify the image here using a vision model
        # detected_template = classify_meme_template(filepath)
        
        return jsonify({"success": True, "filename": filename})
    
    return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
