def filter_chosen_word(top_words, chosen_word):
    filtered_list = [word for word in top_words if word == chosen_word]
    print("원래 리스트:", top_words)
    print("선택된 단어:", chosen_word)
    print("최종 리스트:", filtered_list)
    return filtered_list
