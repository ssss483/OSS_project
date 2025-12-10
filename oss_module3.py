def filter_words(word_list):

    if not word_list:
        print("단어 리스트가 비어 있습니다.")
        return

    # 남길 단어만 임시로 저장할 리스트
    keep_list = []

    for word in word_list:
        answer = input(f"'{word}' 단어를 대체하겠습니까? (y/n): ").strip().lower()

        # y면 keep_list에 추가
        if answer == "y":
            keep_list.append(word)

        # n이면 추가하지 않음

    # 원본 리스트를 in-place로 수정
    word_list[:] = keep_list
