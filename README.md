Repeated Word Corrector with Huggingface
========================

## 프로젝트 개요
글을 작성할 때 특정 단어를 무의식적으로 반복하면 글의 완성도가 떨어지고, 독자의 몰입을 방해할 수 있다.
이 프로젝트는 이러한 문제를 해결하기 위해 텍스트 내 반복되는 단어를 자동으로 분석하고, 상위 3개의 반복 단어와 그 사용 횟수를 제시한다.
이후 맥락에 맞는 대체 단어를 추천하여 글의 다양성과 표현력을 높이는 것을 목표로 한다.

>>이를 통해 사용자는 자신의 글쓰기 습관을 점검하고, 보다 풍부하고 세련된 가독성 있는 글을 완성할 수 있다.

## 데모나 예시를 보여주는 이미지/영상
### 1. 분석할 문장을 입력한다.
   
<img width="1100" height="150" alt="image" src="https://github.com/user-attachments/assets/ebfb3232-e863-4da9-b963-0876aa299968" />

### 2. 입력된 문장에서 사용된 단어와 빈도수를 확인할 수 있다.

   프로그램은 문장을 분석해 단어별 등장 횟수를 계산하고,
   특히 반복적으로 사용된 단어 상위 3개를 강조하여 보여준다.

   이를 통해 글에서 어떤 단어를 무의식적으로 자주 사용하는지 쉽게 확인할 수 있다.

<img width="280" height="773" alt="스크린샷 2025-12-12 010201" src="https://github.com/user-attachments/assets/28cab7f5-d172-4a5c-9b16-5459e392fca9" />

### 3. 반복된 단어에 대해 대체할지 여부를 선택한다.

   프로그램은 가장 많이 반복된 단어들을 사용자에게 보여주고,
   각 단어를 대체할지 여부를 y/n 옵션으로 직접 선택할 수 있도록 안내한다.
   
   사용자는 필요하다고 판단되는 단어만 골라 자연스럽게 교체함으로써,
   글의 흐름을 유지하면서 표현의 다양성을 높일 수 있다.
   
<img width="500" height="151" alt="image" src="https://github.com/user-attachments/assets/e86bb87e-4ab7-407e-97c9-4b0b347eba55" />

 ### 4. masking 할 문장을 다시 입력받고 masking 된 문장을 확인한다.

   사용자가 대체를 선택한 단어들은 문장 내에서 자동으로 [MASK] 토큰으로 치환된다.
   이 과정은 모델이 문맥에 적합한 새로운 표현을 찾아 적용할 수 있도록 준비하는 단계다.
   
<img width="1100" height="297" alt="image" src="https://github.com/user-attachments/assets/c78e5cb1-814f-41bd-b2cf-238a54e5c1c3" />

### 5. 최종적으로 대체된 문장이 생성된다.
   
   마스킹된 부분에 대해 Hugging Face 모델이 적절한 단어를 예측하여 채워 넣고,
   반복 표현을 최소화한 보다 자연스러운 문장이 완성된다.
   사용자는 반복되는 단어가 제거되고 가독성이 개선된 문장을 최종 결과로 확인할 수 있다.

<img width="1400" height="300" alt="image" src="https://github.com/user-attachments/assets/ed34c685-82f8-4444-90ca-6323238e7d37" />

## 사용한 패키지와 그 version(install 이 필요한 경우 안내)
1. python(3.13.9)
2. Hugging Face Transformers -install 필요
   (아나콘다(미니콘다)설치 --> pip install transformers datasets evaluate accelerate)
3. PyTorch(2.9.1)- install 필요
   (아나콘다(미니콘다)설치 --> pip install torch)

## 실행 방법


## 참고자료
[파이썬으로 간단한 단어 빈도수 분석기 만들기-네이버 블로그](https://m.blog.naver.com/gothevole/223714911712)
