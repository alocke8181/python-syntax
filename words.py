def print_uppper_words(words, must_start_with):
    """Prints all words in that start with the specified letters in uppercase"""
    for word in words:
        if(word[0] in must_start_with):
            print(word.upper())

print_uppper_words(["hello","hey","goodbye","yo","yes"],["h","y"])