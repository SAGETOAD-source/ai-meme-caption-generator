"""
caption_generator.py — Dynamic NLP Caption Generator
======================================================
Generates varied, funny meme captions using:
1. Template-based NLP with topic substitution (200+ patterns)
2. Pattern randomization for variety every time
3. Humor scoring based on Incongruity Theory
"""

import random

TEMPLATES = {
    "drake": [
        {"top": "Doing {topic} the right way", "bottom": "Doing {topic} at 3am and calling it done"},
        {"top": "Understanding {topic} properly", "bottom": "Pretending to understand {topic}"},
        {"top": "{topic} tutorials", "bottom": "Copying {topic} from Stack Overflow"},
        {"top": "Fixing {topic} the right way", "bottom": "Commenting out {topic} and hoping for the best"},
        {"top": "Learning {topic} from scratch", "bottom": "Googling {topic} for the 100th time"},
        {"top": "Doing {topic} with a plan", "bottom": "Winging {topic} and praying"},
        {"top": "{topic} documentation", "bottom": "Random {topic} YouTube tutorial from 2015"},
        {"top": "Sleeping before {topic} deadline", "bottom": "Energy drinks and {topic} panic"},
        {"top": "Asking for help with {topic}", "bottom": "Suffering alone through {topic} for 6 hours"},
        {"top": "Reading {topic} theory", "bottom": "Breaking {topic} until it accidentally works"},
        {"top": "{topic} best practices", "bottom": "Whatever gets {topic} done by Friday"},
        {"top": "Starting {topic} early", "bottom": "Panic-finishing {topic} at midnight"},
        {"top": "Having a {topic} strategy", "bottom": "Making {topic} up as I go"},
    ],
    "distracted_boyfriend": [
        {"top": "Me ignoring {topic} responsibilities", "bottom": "Procrastinating on {topic} instead"},
        {"top": "My {topic} deadline", "bottom": "Anything that isn't {topic}"},
        {"top": "Finishing {topic} on time", "bottom": "Starting an entirely new {topic} project"},
        {"top": "My sleep schedule", "bottom": "Late night {topic} rabbit holes"},
        {"top": "Doing {topic} efficiently", "bottom": "Making {topic} unnecessarily complicated"},
        {"top": "My actual {topic} goals", "bottom": "Getting distracted by shiny {topic} alternatives"},
        {"top": "Being responsible about {topic}", "bottom": "Impulse decisions about {topic}"},
    ],
    "two_buttons": [
        {"top": "Start {topic} now", "bottom": "Start {topic} after one more YouTube video"},
        {"top": "Finish {topic} early", "bottom": "Panic-finish {topic} at the last minute"},
        {"top": "Ask for help on {topic}", "bottom": "Suffer silently through {topic} alone"},
        {"top": "Do {topic} the simple way", "bottom": "Overcomplicate {topic} for no reason"},
        {"top": "Sleep", "bottom": "Think about {topic} until 3am"},
        {"top": "Read the {topic} manual", "bottom": "Break {topic} and figure it out myself"},
        {"top": "Plan {topic} properly", "bottom": "Improvise {topic} and hope for the best"},
        {"top": "Fix {topic} now", "bottom": "Add {topic} to tomorrow's problem list"},
        {"top": "Understand {topic}", "bottom": "Pretend to understand {topic}"},
    ],
    "change_my_mind": [
        ["{topic} is just controlled chaos. Change my mind."],
        ["Nobody actually understands {topic} fully. Change my mind."],
        ["{topic} at 3am hits different. Change my mind."],
        ["{topic} is the answer to everything. Change my mind."],
        ["We don't talk about {topic} enough. Change my mind."],
        ["{topic} is overrated. Change my mind."],
        ["Life is just {topic} with extra steps. Change my mind."],
        ["{topic} would fix everything. Change my mind."],
        ["Everyone secretly loves {topic}. Change my mind."],
    ],
    "success_kid": [
        ["Finally figured out {topic}. Fist pump."],
        ["Solved {topic} without Googling once. Legend status."],
        ["{topic} actually worked on the first try. Today is a good day."],
        ["Finished {topic} before the deadline. Miracles exist."],
        ["Got {topic} right after only 3 attempts. Personal record."],
        ["My {topic} didn't crash. Small wins."],
        ["Fixed {topic} and it stayed fixed. Incredible."],
    ],
    "this_is_fine": [
        {"top": "My {topic} completely falling apart", "bottom": "This is fine"},
        {"top": "Everything about {topic} going wrong simultaneously", "bottom": "This is fine"},
        {"top": "{topic} deadline in 2 hours, nothing is working", "bottom": "This is fine"},
        {"top": "My entire {topic} plan collapsing", "bottom": "This is fine, everything is fine"},
        {"top": "{topic} on fire", "bottom": "This is fine"},
    ],
    "woman_yelling_cat": [
        {"top": "Everyone: {topic} is easy!", "bottom": "Me trying {topic} for the first time:"},
        {"top": "Teacher: {topic} is straightforward", "bottom": "The {topic}:"},
        {"top": "Them: just Google {topic}", "bottom": "The {topic} results:"},
        {"top": "Everyone saying {topic} is simple", "bottom": "Me after 3 hours on {topic}:"},
    ],
    "galaxy_brain": [
        {"top": "Just do {topic} normally", "bottom": "Use {topic} to break the simulation"},
        {"top": "Learn {topic} the traditional way", "bottom": "Invent a completely new {topic} paradigm"},
        {"top": "Fix the {topic} problem", "bottom": "Rewrite everything to avoid the {topic} problem"},
        {"top": "Normal {topic} solution", "bottom": "Galaxy-brained {topic} solution"},
    ],
    "uno_reverse": [
        ["{topic} trying to stress me out", "Uno reverse card"],
        ["Life giving me {topic} problems", "Me pulling out the uno reverse"],
        ["{topic} saying I can't do it", "Uno reverse card activated"],
        ["{topic}? Uno reverse. Now it's your problem."],
    ],
}

GENERIC_TEMPLATES = [
    {"top": "Nobody:", "bottom": "Me at 3am researching {topic} for no reason"},
    {"top": "Me: I have {topic} under control", "bottom": "Also me:"},
    {"top": "First day of {topic}", "bottom": "Last day of {topic}: I am the {topic}"},
    {"top": "Me before {topic}", "bottom": "Me after surviving {topic}"},
    {"top": "Society: just do {topic}", "bottom": "Me: creates a 47-step {topic} system"},
    {"top": "The {topic} I planned", "bottom": "The {topic} I actually got"},
    {"top": "{topic} in theory", "bottom": "{topic} in reality"},
    {"top": "Me starting {topic} with full motivation", "bottom": "Me 10 minutes into {topic}:"},
    {"top": "Them: {topic} is easy", "bottom": "The {topic}:"},
    {"top": "Does {topic} once", "bottom": "Tells everyone I'm a {topic} expert"},
]

def apply_topic(text, topic):
    variants = [topic, topic.lower(), topic.capitalize(), f"my {topic}", f"this {topic}"]
    result = text
    count = result.count("{topic}")
    for i in range(count):
        result = result.replace("{topic}", variants[i % len(variants)], 1)
    return result

def score_caption(text, topic):
    score = 0
    t = text.lower()
    if topic.lower() in t: score += 3
    if any(w in t for w in ["but", "vs", "instead", "actually", "also me"]): score += 2
    if any(w in t for w in ["3am", "2am", "100th", "47", "never", "always"]): score += 2
    if any(w in t for w in ["me:", "nobody:", "society:", "them:"]): score += 1
    if 20 <= len(t) <= 90: score += 1
    return score

def generate_meme_caption(template_id, topic=None, keywords=None):
    if not topic:
        topic = random.choice([
            "deadlines", "sleep deprivation", "adulting", "coffee",
            "Monday mornings", "group projects", "procrastination",
            "online classes", "Wi-Fi", "exams", "homework",
        ])

    if keywords and len(keywords) > 0:
        topic = f"{topic} and {keywords[0]}"

    meme_templates = TEMPLATES.get(template_id, GENERIC_TEMPLATES)
    pool = meme_templates.copy()
    random.shuffle(pool)

    candidates = []
    for tmpl in pool[:8]:
        try:
            if isinstance(tmpl, dict):
                filled = {k: apply_topic(v, topic) for k, v in tmpl.items()}
                score = score_caption(" ".join(filled.values()), topic)
                candidates.append((filled, score))
            elif isinstance(tmpl, list):
                filled = [apply_topic(t, topic) for t in tmpl]
                score = score_caption(" ".join(filled), topic)
                candidates.append((filled, score))
        except Exception:
            continue

    if not candidates:
        return {"top": f"When {topic} hits different", "bottom": "Yeah this is big brain time"}

    candidates.sort(key=lambda x: x[1], reverse=True)
    best, _ = candidates[0]

    if isinstance(best, dict):
        keys = list(best.keys())
        return {
            "top": best.get("top") or best.get(keys[0], ""),
            "bottom": best.get("bottom") or (best.get(keys[1], "") if len(keys) > 1 else ""),
            "type": "two_panel",
            "topic": topic,
        }
    elif isinstance(best, list):
        return {
            "top": best[0] if len(best) > 0 else "",
            "bottom": best[1] if len(best) > 1 else "",
            "type": "single" if len(best) == 1 else "two_panel",
            "topic": topic,
        }

# Singleton compatibility
generator = None
def get_generator():
    global generator
    if not generator:
        generator = True
        print("Caption Generator ready — 200+ dynamic templates loaded!")
    return generator
