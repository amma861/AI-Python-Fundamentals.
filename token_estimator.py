def estimate_tokens(text):
    """
    A simple BPE-style (Byte Pair Encoding) logic.
    On average, 1 token is about 4 characters in English.
    """
    char_count = len(text)
    estimated_tokens = math.ceil(char_count / 4)
    
    # Also counting unique words to understand 'Lexical Diversity'
    words = text.lower().split()
    unique_words = len(set(words))
    
    return {
        "char_count": char_count,
        "token_estimate": estimated_tokens,
        "unique_words": unique_words
    }

sample_input = "AI safety is the most important research field in the 21st century."
stats = estimate_tokens(sample_input)

print(f"Analysis for: '{sample_input}'")
print(f"Estimated Tokens: {stats['token_estimate']}")
print(f"Lexical Diversity: {stats['unique_words']} unique words.")
