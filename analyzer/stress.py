import string
import pronouncing
import re


# Hardcoded noun/verb stress pattern mappings
NOUN_VERB_STRESS_PATTERNS = {
    'record': {'noun': [0, 1], 'verb': [1, 0]},
    'present': {'noun': [1, 0], 'verb': [0, 1]},
    'project': {'noun': [1, 0], 'verb': [0, 1]},
    'object': {'noun': [1, 0], 'verb': [0, 1]},
    'subject': {'noun': [1, 0], 'verb': [0, 1]},
    'contract': {'noun': [1, 2], 'verb': [0, 1]},
    'address': {'noun': [1, 2], 'verb': [0, 1]},
    'content': {'noun': [1, 0], 'verb': [0, 1]},
    'desert': {'noun': [1, 0], 'verb': [0, 1]},
    'refuse': {'noun': [1, 2], 'verb': [0, 1]},
    'produce': {'noun': [1, 0], 'verb': [0, 1]}
}


def detect_pos_simple(word, context):
    """
    Simple pattern-based POS detection for common noun/verb pairs
    Returns 'noun', 'verb', or 'unknown'
    """
    if not context:
        return 'unknown'
    
    word_lower = word.lower()
    context_lower = context.lower()
    
    # Look for verb indicators in context
    verb_patterns = [
        r'\b(to|will|would|can|could|should|must|may|might)\s+' + re.escape(word_lower),
        r'\b(I|you|we|they|he|she|it)\s+' + re.escape(word_lower),
        r'\b' + re.escape(word_lower) + r'\s+(the|a|an|this|that|these|those)',
        r'\b' + re.escape(word_lower) + r'ed\b',
        r'\b' + re.escape(word_lower) + r'ing\b'
    ]
    
    # Look for noun indicators
    noun_patterns = [
        r'\b(the|a|an|this|that|these|those)\s+' + re.escape(word_lower),
        r'\b' + re.escape(word_lower) + r'\s+(is|are|was|were)',
        r'\b' + re.escape(word_lower) + r's\b'  # plural
    ]
    
    for pattern in verb_patterns:
        if re.search(pattern, context_lower):
            return 'verb'
    
    for pattern in noun_patterns:
        if re.search(pattern, context_lower):
            return 'noun'
    
    return 'unknown'


def get_word_stress(word, context="", pos_hint=None):
    """
    Get the stress pattern for a word as a list of integers
    Returns None if the word is not found
    
    Args:
        word: The word to analyze
        context: Optional context string for POS detection
        pos_hint: Optional explicit POS hint ('noun' or 'verb')
    """
    word_clean = word.lower().strip(string.punctuation)
    
    # Check if this word has noun/verb variants
    if word_clean in NOUN_VERB_STRESS_PATTERNS:
        if pos_hint and pos_hint in NOUN_VERB_STRESS_PATTERNS[word_clean]:
            return NOUN_VERB_STRESS_PATTERNS[word_clean][pos_hint]
        else:
            pos = detect_pos_simple(word_clean, context)
            if pos in NOUN_VERB_STRESS_PATTERNS[word_clean]:
                return NOUN_VERB_STRESS_PATTERNS[word_clean][pos]
    
    # Fallback to original pronunciation lookup
    phones = pronouncing.phones_for_word(word_clean)
    if not phones:
        return None
    return [int(s) for s in pronouncing.stresses(phones[0])]

def get_line_stress(line):
    
    """

    Get the stress pattern for a line as a list of dictionaries with the format {'word': word, 'stress': stress}
    If a word is not found, it will return {'word': "none", 'stress': []}
    """ 
    
    words = line.split()
    stresses = []
    for word in words:
        # Pass the full line as context for POS detection
        stress = get_word_stress(word, line)
        if stress is not None:
            stresses.append({'word': word, 'stress': stress})
        if stress is None:
            stresses.append({'word': "none", 'stress': []})
    return stresses