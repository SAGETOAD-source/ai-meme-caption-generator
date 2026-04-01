"""
AI Caption Generator Module
===========================
Provides AI-enhanced caption generation using HuggingFace Transformers.

This module attempts to use GPT-2 or similar models for creative caption
generation. Falls back gracefully if transformers are not installed.

Features:
- GPT-2 based text generation
- Template-aware prompting
- Configurable creativity/temperature
- Fallback to template-based generation

Author: College Mini Project
"""

import random
import os

# ============================================
# Optional AI Model Loading
# ============================================

TRANSFORMERS_AVAILABLE = False
generator = None

# Try to import transformers (optional dependency)
try:
    from transformers import pipeline, set_seed
    import torch
    TRANSFORMERS_AVAILABLE = True
    print("Transformers library available - AI generation enabled")
except ImportError:
    print("Transformers not installed - using template-based generation only")

def load_ai_model(model_name="gpt2"):
    """
    Load the AI text generation model.

    Args:
        model_name: Name of the model to load (default: gpt2)

    Returns:
        Text generation pipeline or None if unavailable
    """
    global generator

    if not TRANSFORMERS_AVAILABLE:
        print("Transformers library not available")
        return None

    if generator is not None:
        return generator

    try:
        print(f"Loading {model_name} model...")

        # Configure for CPU if CUDA unavailable
        device = 0 if torch.cuda.is_available() else -1

        generator = pipeline(
            'text-generation',
            model=model_name,
            device=device,
            torch_dtype=torch.float32 if device == -1 else torch.float16
        )

        print(f"Model {model_name} loaded successfully!")
        return generator

    except Exception as e:
        print(f"Failed to load model: {e}")
        return None

# ============================================
# Template Prompts for AI Generation
# ============================================

TEMPLATE_PROMPTS = {
    "drake": [
        "Create a funny comparison about {topic}:",
        "Write a Drake meme caption about {topic}. Top panel (rejected):",
        "Generate a relatable meme about {topic}. Bad option:",
    ],
    "distracted-boyfriend": [
        "Create a distracted boyfriend meme about {topic}:",
        "Write a funny caption about being distracted from {topic}:",
    ],
    "two-buttons": [
        "Create a difficult choice meme about {topic}:",
        "Write a meme about choosing between two {topic} options:",
    ],
    "change-my-mind": [
        "Write a bold opinion about {topic}:",
        "Create a controversial take on {topic}:",
    ],
    "success-kid": [
        "Write a success story about {topic}:",
        "Create a caption about achieving something with {topic}:",
    ],
    "this-is-fine": [
        "Write a denial meme about {topic}:",
        "Create a caption pretending {topic} is fine when it's not:",
    ],
    "custom": [
        "Write a funny meme caption about {topic}:",
        "Create a humorous caption for a meme about {topic}:",
    ]
}

# ============================================
# AI Generation Functions
# ============================================

def generate_with_ai(template_id, topic=None, keywords=None, temperature=0.8, max_length=50):
    """
    Generate a meme caption using AI model.

    Args:
        template_id: The meme template ID
        topic: Optional topic for context
        keywords: Optional list of keywords to include
        temperature: Creativity level (0.0-1.0)
        max_length: Maximum length of generated text

    Returns:
        Dict with top and bottom caption text
    """
    global generator

    # Ensure model is loaded
    if generator is None:
        generator = load_ai_model()

    if generator is None:
        raise ImportError("AI model not available")

    # Prepare prompt
    if not topic:
        topic = random.choice([
            "programming", "studying", "work", "sleep",
            "coffee", "deadlines", "procrastination"
        ])

    # Get template-specific prompts
    prompts = TEMPLATE_PROMPTS.get(template_id, TEMPLATE_PROMPTS["custom"])
    base_prompt = random.choice(prompts).format(topic=topic)

    # Add keywords to prompt if provided
    if keywords and len(keywords) > 0:
        base_prompt += f" Keywords: {', '.join(keywords)}."

    # Set random seed for reproducibility
    set_seed(random.randint(1, 10000))

    # Generate text
    try:
        outputs = generator(
            base_prompt,
            max_length=max_length,
            num_return_sequences=3,
            temperature=temperature,
            do_sample=True,
            top_p=0.9,
            truncation=True
        )

        # Extract generated text
        candidates = []
        for output in outputs:
            text = output['generated_text']
            # Remove the prompt from the generated text
            text = text.replace(base_prompt, "").strip()
            candidates.append(text)

        # Format for meme template
        return format_for_template(template_id, candidates[0], candidates[1] if len(candidates) > 1 else "")

    except Exception as e:
        print(f"AI generation failed: {e}")
        raise

def format_for_template(template_id, text1, text2=""):
    """
    Format AI-generated text for specific meme templates.

    Args:
        template_id: The meme template
        text1: Primary generated text
        text2: Secondary generated text (optional)

    Returns:
        Dict with top and bottom text
    """
    # Clean up generated text
    text1 = text1.strip().replace('"', '').replace("'", "")
    text2 = text2.strip().replace('"', '').replace("'", "")

    # Split long text into sentences for top/bottom
    if not text2 and len(text1) > 30:
        sentences = text1.split('. ')
        if len(sentences) >= 2:
            text1 = sentences[0]
            text2 = '. '.join(sentences[1:])

    # Template-specific formatting
    if template_id == "drake":
        return {
            "top": text1 or "The wrong way",
            "bottom": text2 or "The right way",
            "type": "comparison"
        }
    elif template_id == "distracted-boyfriend":
        return {
            "top": "Me",
            "bottom": text1 or "My responsibilities",
            "other": text2 or "Distraction",
            "type": "labels"
        }
    elif template_id == "two-buttons":
        return {
            "top": text1 or "Option A",
            "bottom": text2 or "Option B",
            "type": "choice"
        }
    elif template_id == "change-my-mind":
        return {
            "top": text1 or f"{text2} is the best. Change my mind.",
            "bottom": "",
            "type": "single"
        }
    elif template_id == "success-kid":
        return {
            "top": text1 or "Finally did it",
            "bottom": text2 or "Didn't mess up",
            "type": "top-bottom"
        }
    else:
        return {
            "top": text1,
            "bottom": text2,
            "type": "top-bottom"
        }

def score_ai_caption(text, topic):
    """
    Score AI-generated caption for quality and humor.

    Args:
        text: The generated caption
        topic: The topic context

    Returns:
        Float score (higher is better)
    """
    score = 0.0
    t = text.lower()

    # Topic relevance
    if topic and topic.lower() in t:
        score += 3.0

    # Humor indicators
    humor_words = ['but', 'vs', 'instead', 'actually', 'also', 'meanwhile']
    for word in humor_words:
        if word in t:
            score += 1.0

    # Length preference (not too short, not too long)
    word_count = len(text.split())
    if 5 <= word_count <= 20:
        score += 2.0
    elif 3 <= word_count <= 30:
        score += 1.0

    # Contrast and comparison bonus
    if any(w in t for w in ['better', 'worse', 'right', 'wrong', 'good', 'bad']):
        score += 1.5

    return score

# ============================================
# Hybrid Generation
# ============================================

def hybrid_generate(template_id, topic=None, keywords=None):
    """
    Combine template-based and AI generation for best results.

    Uses AI to enhance template-based captions with more variety
    and creativity while maintaining structural coherence.

    Args:
        template_id: The meme template
        topic: Optional topic
        keywords: Optional keywords

    Returns:
        Dict with caption data
    """
    # Get base template caption
    from caption_generator import generate_meme_caption
    base_caption = generate_meme_caption(template_id, topic, keywords)

    # Try to enhance with AI if available
    try:
        if generator is not None:
            ai_caption = generate_with_ai(template_id, topic, keywords)

            # Combine - use AI text but ensure structural validity
            if ai_caption.get('top') and len(ai_caption['top']) > 5:
                base_caption['top'] = ai_caption['top']

            if ai_caption.get('bottom') and len(ai_caption['bottom']) > 5:
                base_caption['bottom'] = ai_caption['bottom']

    except Exception as e:
        print(f"AI enhancement failed, using base caption: {e}")

    return base_caption

# ============================================
# Initialization
# ============================================

# Auto-load model on import if transformers available
if TRANSFORMERS_AVAILABLE:
    # Don't auto-load to avoid slow startup - load on first use instead
    print("AI Generator ready (model will load on first use)")
else:
    print("AI Generator: Template-based mode only")
