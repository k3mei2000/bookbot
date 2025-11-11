def get_word_count(book_text):
    return len(str.split(book_text))

def get_character_count(book_text):
    char_counts = {}
    for char in book_text:
        lower_char = str.lower(char)
        if lower_char not in char_counts:
            char_counts[lower_char] = 1
        else:
            char_counts[lower_char] += 1
    return char_counts

def sort_on(items):
    return items["num"]

def get_sorted_character_counts(char_counts):
    sorted_char_counts = []
    for key in char_counts:
        sorted_char_counts.append({"char": key, "num": char_counts[key]})
    sorted_char_counts.sort(reverse=True, key=sort_on)
    return sorted_char_counts
    