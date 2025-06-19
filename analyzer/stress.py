import string
import pronouncing


def get_word_stress(word):
    """
    Get the stress pattern for a word as a list of integers
    Returns None if the word is not found
    """
    word = word.lower().strip(string.punctuation)
    phones = pronouncing.phones_for_word(word)
    if not phones:
        return None
    # Get the first pronunciation's stress pattern
    return [int(s) for s in pronouncing.stresses(phones[0])]

def get_line_stress(line):
    
    """

    Get the stress pattern for a line as a list of dictionaries with the format {'word': word, 'stress': stress}
    If a word is not found, it will return {'word': "none", 'stress': []}
    """ 
    
    words = line.split()
    stresses = []
    for word in words:
        stress = get_word_stress(word)
        if stress is not None:
            stresses.append({'word': word, 'stress': stress})
        if stress is None:
            stresses.append({'word': "none", 'stress': []})
    return stresses