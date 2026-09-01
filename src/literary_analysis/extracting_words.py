def extract_words(text, special_signs=()):
    words = []
    word = ""

    for sign in text:
        if sign.isalpha() or (sign in special_signs):   #special signs that are part of our words (like ' or -)
            word += sign.lower()  # we will write down all words in lower case to not duplicate them
        else:
            if word != "":
                words.append(word)
                word = ""

    if word != "":
        words.append(word)

    return words

def extract_dictionary_words(text, special_signs=()):   #We know that dictionary will have a specific form
    in_lower_caps = [word.lower() for word in text.strip().split(", ")]
    return in_lower_caps
