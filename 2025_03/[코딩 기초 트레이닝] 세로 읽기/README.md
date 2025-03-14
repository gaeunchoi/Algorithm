# [프로그래머스 코딩 기초 트레이닝] 세로 읽기

### 성능 요약

- py
  메모리 | 9.05MB  
  시간 | 0.01ms

- js
  메모리 | 33.5MB  
  시간 | 0.05ms

### 분류

문자열

### 제출 일자

2025-03-14 16:39:34

### 문제 설명

문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

### 제한 사항

- my_string은 영소문자로 이루어져 있습니다.
- 1 ≤ m ≤ my_string의 길이 ≤ 1,000
- m은 my_string 길이의 약수로만 주어집니다.
- 1 ≤ c ≤ m

### 입출력 예

| my_string              | m   | c   | result        |
| ---------------------- | --- | --- | ------------- |
| "ihrhbakrfpndopljhygc" | 4   | 2   | "happy"       |
| "programmers"          | 1   | 1   | "programmers" |
