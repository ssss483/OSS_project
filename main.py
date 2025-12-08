# main.py

from module1 import calc_word_frequency
from module2 import get_top3_words
from module3 import filter_words
from module4 import masking
from module5 import apply_fill_mask

WORD_LIST = []
INPUT_SENTENCE = ""


def main():
    global WORD_LIST, INPUT_SENTENCE

    print("텍스트를 입력하세요. (끝내려면 빈 줄 입력 후 Enter)\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)

    freq = calc_word_frequency(text)

    print("\n=== 단어 빈도수 ===")
    for word, count in freq.items():
        print(word, ":", count)

    WORD_LIST = get_top3_words(freq)
    print("\n상위 단어 리스트(전역):", WORD_LIST)

    WORD_LIST = filter_words(WORD_LIST)
    print("선택된 단어 리스트(전역):", WORD_LIST)

    print("\n마스킹할 문장을 입력하세요.")
    INPUT_SENTENCE = input("문장: ").strip()
    print("입력된 문장(전역):", INPUT_SENTENCE)

    masked_sentence = masking(WORD_LIST, INPUT_SENTENCE)
    print("\n마스킹된 문장:", masked_sentence)

    completed_sentence = apply_fill_mask(masked_sentence)

    print("\n=== 최종 문장 ===")
    print(completed_sentence)


if __name__ == "__main__":
    main()

