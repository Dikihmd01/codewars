def reverse_words(s):
    lists = s.split()
    lists = list(reversed(lists))

    return " ".join(lists)
