def print_upper_words(words):
    """Print each word to upper-case"""
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """Print each word to upper-case that starts with an e"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """Print each word to upper-case that starts with words in required set"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())