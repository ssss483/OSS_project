from transformers import pipeline

# 1. fill-mask 파이프라인 준비
fill_mask = pipeline("fill-mask", model="bert-base-uncased")

# 2. 상위 3개 단어가 이미 리스트에 저장되어 있다고 가정
top_words = ["love", "play", "football"]

# 3. 사용자가 대체할 단어를 선택 (예: "play")
chosen_word = "play"

# 4. fill-mask로 대체 후보 생성
masked_sentence = f"I {chosen_word} [MASK] everyday"
predictions = fill_mask(masked_sentence)

# 5. 가장 확률 높은 후보 단어 선택
replacement = predictions[0]["token_str"]

# 6. 리스트에서 chosen_word만 남기고 나머지 제거
filtered_list = [chosen_word]

print("원래 리스트:", top_words)
print("선택된 단어:", chosen_word)
print("대체된 결과:", replacement)
print("최종 리스트:", filtered_list)