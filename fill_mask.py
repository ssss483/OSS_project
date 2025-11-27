from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model = "klue/roberta-base"
)


ressult = fill_mask("오늘은 날씨가 정말 <mask>다")

for r in result:
    print(r)