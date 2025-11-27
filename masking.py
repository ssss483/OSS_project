def masking(word_list, sentence):
    for w in word_list:
        sentence=sentence.replace(w, "[MASK]")
    return sentence

