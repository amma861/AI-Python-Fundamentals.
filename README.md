# AI-Python-Fundamentals.
"This repo tracks my transition from Java to Python, specifically focusing on Natural Language Processing logic for AI applications."


# Semantic Text Analyzer for OpenAI Residency Prep
# Author: Ani Faith Chison

def analyze_text(text):
    print(f"--- Analyzing: '{text}' ---")
    
    # 1. Tokenization: Breaking the sentence into individual words
    words = text.lower().split()
    word_count = len(words)
    
    # 2. Keyword Detection (Simulating 'Attention')
    # AI models look for "important" words to understand context
    impact_words = ["ai", "future", "logic", "intelligence", "open"]
    found_keywords = [word for word in words if word in impact_words]
    
    # 3. Simple Sentiment Logic
    # In AI, we assign numerical values to emotions
    positive_words = ["beneficial", "safe", "great", "innovative"]
    score = sum(1 for word in words if word in positive_words)

    # Output Results
    print(f"Total Tokens: {word_count}")
    print(f"Keywords Found: {found_keywords}")
    print(f"Sentiment Score: {score} (higher is more positive)")
    print("-" * 30)

# Test the function
sample_text = "Building safe and beneficial AI is the future of logic."
analyze_text(sample_text)
