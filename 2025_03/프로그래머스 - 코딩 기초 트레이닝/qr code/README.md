# [프로그래머스 코딩 기초 트레이닝] qr code

### 성능 요약

- py  
  메모리 | 9.15MB  
  시간 | 0.00ms

- js  
  메모리 | 33.5MB  
  시간 | 0.04ms

### 분류

문자열

### 제출 일자

2025-03-18 15:13:59

### 문제 설명

두 정수 q, r과 문자열 code가 주어질 때, code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

### 제한 사항

- 0 ≤ r < q ≤ 20
- r < code의 길이 ≤ 1,000
- code는 영소문자로만 이루어져 있습니다.

### 입출력 예

| q   | r   | code               |               | result |
| --- | --- | ------------------ | ------------- | ------ |
| 3   | 1   | "qjnwezgrpirldywt" | "jerry"       |
| 1   | 0   | "programmers"      | "programmers" |
