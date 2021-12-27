def order(sentence):
    words = sentence.split()
    return " ".join(sorted(words, key=get_int))

def get_int(word):
    for char in word:
        if char.isdigit():
            return int(char)
    return None
