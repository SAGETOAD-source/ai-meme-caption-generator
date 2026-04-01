# AI-Based Meme Caption Generator

A college mini project that demonstrates Natural Language Processing (NLP) techniques for automatically generating humorous meme captions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![React](https://img.shields.io/badge/React-18.0+-61DAFB.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6.svg)

## Overview

This project implements an AI-powered meme caption generator that:
- Accepts meme template selection as input
- Generates context-aware, humorous captions using NLP pattern matching
- Demonstrates integration of AI with web technologies (React + Flask)
- Supports multiple popular meme templates

## Demo

[Add screenshot or GIF here showing the app in action]

## Features

- **Template Selection**: Choose from 6 popular meme formats (Drake, Distracted Boyfriend, Two Buttons, etc.)
- **Topic-Aware Generation**: Enter a topic for context-aware captions
- **NLP-Based Humor**: Uses pattern matching and humor scoring algorithms
- **Responsive UI**: Clean, modern interface built with React and Tailwind CSS
- **RESTful API**: Well-documented backend endpoints

## Architecture

```
┌─────────────┐      HTTP/JSON       ┌─────────────┐
│   React     │  ◄────────────────►  │    Flask    │
│  Frontend   │                        │   Backend   │
│  (Port      │                        │   (Port     │
│   5173)     │                        │   5000)     │
└─────────────┘                        └──────┬──────┘
                                            │
                                     ┌──────┴──────┐
                                     │   Caption   │
                                     │  Generator  │
                                     │   (NLP)     │
                                     └─────────────┘
```

## Tech Stack

**Frontend:**
- React 18
- TypeScript
- Tailwind CSS
- Vite

**Backend:**
- Python 3.8+
- Flask
- Flask-CORS

**NLP:**
- Template-based pattern matching
- Topic substitution
- Humor scoring (Incongruity Theory)
- Optional: HuggingFace Transformers (GPT-2)

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js 16+ and npm

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/meme-caption-generator.git
cd meme-caption-generator
```

### Step 2: Setup Backend

```bash
cd python_backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend
python app.py
```

The backend will start on `http://localhost:5000`

### Step 3: Setup Frontend

```bash
# In a new terminal, from project root
npm install
npm run dev
```

The frontend will start on `http://localhost:5173`

### Step 4: Open in Browser

Navigate to `http://localhost:5173` to use the application.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/api/templates` | GET | List all meme templates |
| `/api/generate` | POST | Generate meme caption |
| `/api/upload` | POST | Upload custom image |
| `/api/analyze` | POST | Analyze caption quality |

### Example API Request

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "template_id": "drake",
    "topic": "coding",
    "keywords": ["procrastination"]
  }'
```

**Response:**
```json
{
  "success": true,
  "caption": {
    "top": "Doing coding the right way",
    "bottom": "Copying from Stack Overflow",
    "type": "two_panel",
    "topic": "coding"
  },
  "technique": "template_based_nlp"
}
```

## How It Works

### Caption Generation Process

1. **Input**: User selects a meme template and optionally enters a topic
2. **Template Matching**: System loads relevant caption patterns (200+ patterns)
3. **Topic Substitution**: `{topic}` placeholders replaced with user input
4. **Humor Scoring**: Candidates scored based on:
   - Topic relevance (+3)
   - Contrast words: "but", "vs", "instead" (+2)
   - Exaggeration markers: "3am", "always" (+2)
   - Meme structure patterns (+1)
5. **Selection**: Highest scoring caption returned

### Supported Meme Templates

| Template | Type | Description |
|----------|------|-------------|
| Drake Hotline Bling | Comparison | Reject vs Accept format |
| Distracted Boyfriend | Labels | Three-label format |
| Two Buttons | Choice | Difficult decision |
| Change My Mind | Single | Bold opinion statement |
| Success Kid | Top-Bottom | Achievement celebration |
| This is Fine | Top-Bottom | Denial/acceptance |

## Project Structure

```
meme-caption-generator/
├── python_backend/          # Flask backend
│   ├── app.py              # Main Flask application
│   ├── caption_generator.py # NLP caption generation
│   ├── ai_generator.py      # Optional AI enhancement
│   └── requirements.txt     # Python dependencies
├── src/                     # React frontend
│   ├── App.tsx             # Main app component
│   ├── components/         # UI components
│   │   ├── Header.tsx
│   │   ├── TemplateSelector.tsx
│   │   ├── Controls.tsx
│   │   └── MemeCanvas.tsx
│   └── lib/                # Utilities
│       ├── meme-templates.ts
│       └── caption-logic.ts
├── package.json            # Node dependencies
├── tsconfig.json           # TypeScript config
└── vite.config.ts          # Vite config
```

## Evaluation Criteria

This project demonstrates:

1. **NLP Concepts** - Pattern matching, text generation, humor scoring
2. **AI Integration** - Flask web framework, REST API design
3. **Code Quality** - Modular architecture, clear documentation
4. **Functionality** - Multiple templates, context-aware generation
5. **Scalability** - Extensible template system, optional AI enhancement

## Future Enhancements

- [ ] Automatic meme template detection using Computer Vision
- [ ] GPT-3/GPT-4 integration for more creative captions
- [ ] Multi-language caption support
- [ ] Sentiment-based tone adjustment
- [ ] User feedback and rating system
- [ ] Social media sharing integration

## Screenshots

[Add your screenshots here]

## License

This project is created for educational purposes as a college mini project.

## Acknowledgments

- Meme templates from [Imgflip](https://imgflip.com)
- Built with [Flask](https://flask.palletsprojects.com/) and [React](https://react.dev/)

---

**Author:** [Your Name]
**Course:** [Your Course]
**Institution:** [Your College]
