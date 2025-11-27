import re
from collections import Counter

def calc_word_frequency(text):
    tokens = re.findall(r"[A-Za-z가-힣0-9]+", text.lower())
    freq = Counter(tokens)
    return freq
