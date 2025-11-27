from module1 import calc_word_frequency

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

if __name__ == "__main__":
    main()
