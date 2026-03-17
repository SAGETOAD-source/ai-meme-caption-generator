import random
# In a real production environment, we would load the models:
# from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer

# For this reference implementation, we simulate the NLP logic 
# to show how the components interact without downloading 500MB+ models.

class MemeCaptionGenerator:
    def __init__(self):
        print("Initializing NLP Models...")
        # self.generator = pipeline('text-generation', model='gpt2')
        # self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        
        # Predefined templates to seed the generation for specific meme types
        self.meme_contexts = {
            "drake": {
                "prefix": "Reviewing things.",
                "structure": ["Top: Disliking {topic}", "Bottom: Liking {topic}"]
            },
            "distracted_boyfriend": {
                "prefix": "A situation of betrayal or distraction.",
                "structure": ["Boyfriend: Me", "Girlfriend: {topic}", "Distraction: New shiny {topic}"]
            },
            "two_buttons": {
                "prefix": "A difficult choice.",
                "structure": ["Button 1: {topic} A", "Button 2: {topic} B", "Person: Sweating"]
            }
        }

    def generate(self, template_id, topic=None, keywords=None):
        """
        Generates a caption based on the template and optional topic.
        Uses a mocked NLP approach for the assignment deliverable structure.
        """
        if not topic:
            topic = "life"
            
        context = self.meme_contexts.get(template_id, {})
        
        # In a real implementation using GPT-2:
        # prompt = f"Generate a funny meme caption for a {template_id} meme about {topic}."
        # result = self.generator(prompt, max_length=50, num_return_sequences=1)
        # text = result[0]['generated_text']
        
        # Simulated intelligent response
        if template_id == "drake":
            return {
                "top": f"Doing {topic} the normal way",
                "bottom": f"Doing {topic} using AI code"
            }
        elif template_id == "distracted_boyfriend":
            return {
                "label_bf": "Me",
                "label_gf": "My Responsibilities",
                "label_distraction": f"Writing a {topic} bot"
            }
        elif template_id == "two_buttons":
            return {
                "left": f"Study {topic}",
                "right": f"Procrastinate on {topic}",
                "caption": "Me everyday"
            }
        else:
            # Fallback generic caption
            return {
                "top": f"When you finally understand {topic}",
                "bottom": "But it doesn't compile"
            }

# Singleton instance
generator = MemeCaptionGenerator()

def generate_meme_caption(template_id, topic=None, keywords=None):
    return generator.generate(template_id, topic, keywords)
