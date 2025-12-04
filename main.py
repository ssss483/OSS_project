from module1 import calc_word_frequency
from module2 import get_top3_words
from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="klue/roberta-base"
)

def masking(word_list, sentence):
    for w in word_list:
        sentence = sentence.replace(w, "<mask>")
    return sentence

def main():
    print("텍스트를 입력하세요.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)
    freq = calc_word_frequency(text)

    print("=== 단어 빈도수 ===")
    for word, count in freq.items():
        print(word, ":", count)

    top3 = get_top3_words(freq)

    print("\n마스킹에 사용할 단어들을 모두 입력하세요.")
    print("후보:", top3)
    chosen_words = input("단어들을 공백으로 입력: ").split()

    print("\n마스킹할 문장을 입력하세요.")
    sentence = input("문장: ").strip()

    masked_sentence = masking(chosen_words, sentence)
    print("\n마스킹된 문장:", masked_sentence)

    print("\n=== KLUE RoBERTa 예측 결과 ===")
    predictions = fill_mask(masked_sentence)
    for p in predictions:
        print(p)

if __name__ == "__main__":
    main()
