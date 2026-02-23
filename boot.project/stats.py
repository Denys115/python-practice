def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_chars(chars_dict):
    sorted_list = []
    for char, count in chars_dict.items():
        # Creăm un dicționar mic pentru fiecare literă
        new_dict = {"char": char, "num": count}
        sorted_list.append(new_dict)

    # Sortăm lista după numărul de apariții (descrescător)
    def sort_on(dict):
        return dict["num"]
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
