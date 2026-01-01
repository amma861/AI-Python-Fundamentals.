import math
from collections import Counter

# This project demonstrates a "from-scratch" approach to Sentiment Analysis.
# It connects Statistical Logic (Excel-style) to AI Modeling.

class SimpleSentimentModel:
    def __init__(self):
        # A small "lexicon" (dictionary) of sentiment weights
        self.sentiment_weights = {
            "excellent": 1.0, "great": 0.8, "good": 0.5, "happy": 0.6,
            "terrible": -1.0, "bad": -0.8, "poor": -0.5, "sad": -0.6,
            "slow": -0.4, "fast": 0.4, "efficient": 0.7
        }

    def preprocess_text(self, text):
        """Cleans and tokenizes text (The first step of any AI pipeline)."""
        clean_text = text.lower().replace(".", "").replace("!", "")
        return clean_text.split()

    def analyze(self, text):
        """Calculates a sentiment score based on statistical frequency."""
        tokens = self.preprocess_text(text)
        score = 0
        found_words = 0
        
        for word in tokens:
            if word in self.sentiment_weights:
                score += self.sentiment_weights[word]
                found_words += 1
        
        # Calculate the Mean (Average) sentiment
        return score / found_words if found_words > 0 else 0

# --- DATASET FOR TESTING ---
reviews = [
    "The Java logic was excellent and very efficient.",
    "The performance was slow and the results were poor.",
    "I am happy with the fast progress of my Python learning."
]

model = SimpleSentimentModel()

print("--- AI Sentiment Analysis Results ---")
for r in reviews:
    sentiment_score = model.analyze(r)
    label = "POSITIVE" if sentiment_score > 0 else "NEGATIVE" if sentiment_score < 0 else "NEUTRAL"
    print(f"Review: '{r}'")
    print(f"Score: {sentiment_score:.2f} | Label: {label}\n")

