# [프로그래머스 코딩 기초 트레이닝] 간단한 식 계산하기

### 성능 요약

- py
  메모리 | 9.2MB  
  시간 | 0.02ms

- js
  메모리 | 33.5MB  
  시간 | 0.05ms

### 분류

문자열

### 제출 일자

2025-03-12 15:05:03

### 문제 설명

문자열 binomial이 매개변수로 주어집니다. binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '\*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

### 제한 사항

- 0 ≤ a, b ≤ 40,000
- 0을 제외하고 a, b는 0으로 시작하지 않습니다.

### 입출력 예

| binomial         | result     |
| ---------------- | ---------- |
| "43 + 12"        | 55         |
| "0 - 7777"       | -7777      |
| "40000 \* 40000" | 1600000000 |
