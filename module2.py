def get_top3_words(freq_dict):
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    top3 = [word for word, count in sorted_items[:3]]
    print("상위 3개 단어:", top3)
    return top3
