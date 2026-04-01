"""
AI Meme Caption Generator - Flask Application
=============================================
Main Flask application for the AI-Based Meme Caption Generator project.

Features:
- Template-based and AI-enhanced caption generation
- Image upload handling
- RESTful API endpoints

Author: College Mini Project
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
from werkzeug.utils import secure_filename
from datetime import datetime

# Import caption generation module
from caption_generator import generate_meme_caption

# ============================================
# Flask App Configuration
# ============================================

app = Flask(__name__)
CORS(app)

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ============================================
# Helper Functions
# ============================================

def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def log_request(endpoint, data):
    """Log API requests for debugging."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {endpoint}: {json.dumps(data, indent=2)}")

# ============================================
# API Endpoints
# ============================================

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "AI Meme Caption Generator",
        "version": "1.0.0"
    })

@app.route('/api/templates', methods=['GET'])
def get_templates():
    """Get all available meme templates."""
    templates = [
        {
            "id": "drake",
            "name": "Drake Hotline Bling",
            "description": "Comparison meme - top is bad, bottom is good",
            "type": "comparison",
            "url": "https://i.imgflip.com/30b1gx.jpg"
        },
        {
            "id": "distracted-boyfriend",
            "name": "Distracted Boyfriend",
            "description": "Distracted by new thing",
            "type": "labels",
            "url": "https://i.imgflip.com/1ur9b0.jpg"
        },
        {
            "id": "two-buttons",
            "name": "Two Buttons",
            "description": "Difficult choice between two options",
            "type": "choice",
            "url": "https://i.imgflip.com/1g8my4.jpg"
        },
        {
            "id": "change-my-mind",
            "name": "Change My Mind",
            "description": "Opinion stated with confidence",
            "type": "single",
            "url": "https://i.imgflip.com/24y43o.jpg"
        },
        {
            "id": "success-kid",
            "name": "Success Kid",
            "description": "Small victories and achievements",
            "type": "top-bottom",
            "url": "https://i.imgflip.com/1bip.jpg"
        },
        {
            "id": "this-is-fine",
            "name": "This is Fine",
            "description": "Denial in the face of disaster",
            "type": "top-bottom",
            "url": "https://i.imgflip.com/wxica.jpg"
        }
    ]

    return jsonify({
        "success": True,
        "templates": templates
    })

@app.route('/api/generate', methods=['POST'])
def generate_caption():
    """Generate meme caption using NLP techniques."""
    data = request.json

    if not data:
        return jsonify({
            "success": False,
            "error": "No JSON data provided"
        }), 400

    log_request('/api/generate', data)

    template_id = data.get('template_id')
    topic = data.get('topic', '')
    keywords = data.get('keywords', [])

    if not template_id:
        return jsonify({
            "success": False,
            "error": "template_id is required"
        }), 400

    try:
        caption = generate_meme_caption(template_id, topic, keywords)

        response = {
            "success": True,
            "caption": caption,
            "template_id": template_id,
            "topic": topic,
            "generated_at": datetime.now().isoformat(),
            "technique": "template_based_nlp"
        }

        return jsonify(response)

    except Exception as e:
        print(f"Error generating caption: {str(e)}")
        return jsonify({
            "success": False,
            "error": f"Caption generation failed: {str(e)}"
        }), 500

@app.route('/api/upload', methods=['POST'])
def upload_image():
    """Handle meme image uploads."""
    if 'file' not in request.files:
        return jsonify({
            "success": False,
            "error": "No file provided"
        }), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({
            "success": False,
            "error": "No file selected"
        }), 400

    if file and allowed_file(file.filename):
        try:
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{filename}"

            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            return jsonify({
                "success": True,
                "filename": filename,
                "url": f"/uploads/{filename}",
                "message": "File uploaded successfully"
            })

        except Exception as e:
            return jsonify({
                "success": False,
                "error": f"File upload failed: {str(e)}"
            }), 500

    return jsonify({
        "success": False,
        "error": "Invalid file type. Allowed: PNG, JPG, JPEG, GIF"
    }), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded images."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/api/analyze', methods=['POST'])
def analyze_caption():
    """Analyze caption humor and quality."""
    data = request.json

    if not data or 'caption' not in data:
        return jsonify({
            "success": False,
            "error": "caption is required"
        }), 400

    caption = data.get('caption', '')

    analysis = {
        "length": len(caption),
        "word_count": len(caption.split()),
        "has_contrast": any(word in caption.lower() for word in ['but', 'vs', 'instead', 'actually']),
        "has_exaggeration": any(word in caption.lower() for word in ['always', 'never', 'everything', 'nothing']),
        "humor_indicators": {
            "relatability": "relatable situation" in caption.lower(),
            "wordplay": len(set(caption.lower().split())) < len(caption.split()) * 0.8
        }
    }

    return jsonify({
        "success": True,
        "analysis": analysis,
        "caption": caption
    })

# ============================================
# Error Handlers
# ============================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500

# ============================================
# Main Entry Point
# ============================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

    print(f"=" * 50)
    print(f"AI Meme Caption Generator")
    print(f"Starting server on port {port}")
    print(f"Debug mode: {debug}")
    print(f"=" * 50)

    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
