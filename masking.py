# module4.py
import re

def masking(word_list, sentence):
    for w in word_list:
        sentence = re.sub(rf"\b{re.escape(w)}\b", "[MASK]", sentence)
    return sentence
