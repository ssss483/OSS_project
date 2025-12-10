# module 5
from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="klue/roberta-base",
    tokenizer="klue/roberta-base"
)

def apply_fill_mask(masked_sentence):
    sentence = masked_sentence

    while "[MASK]" in sentence:

        preds = fill_mask(sentence)

        # CASE 1: preds = [ {dict}, {dict}, ... ]
        if isinstance(preds[0], dict):
            best_token = preds[0]["token_str"].strip()

        # CASE 2: preds = [ [ {dict}, {dict}, ... ] ]
        elif isinstance(preds[0], list) and isinstance(preds[0][0], dict):
            best_token = preds[0][0]["token_str"].strip()

        else:
            # 예측 불가능한 구조 → MASK 제거
            best_token = ""

        # 첫 번째 MASK만 치환
        sentence = sentence.replace("[MASK]", best_token, 1)

    return sentence
