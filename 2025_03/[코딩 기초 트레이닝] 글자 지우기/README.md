# [프로그래머스 코딩 기초 트레이닝] 글자 지우기

### 성능 요약

- py
  메모리 | 9.1MB  
  시간 | 0.02ms

- js
  메모리 | 33.5MB  
  시간 | 0.05ms

### 분류

리스트(배열)

### 제출 일자

2025-03-14 17:10:32

### 문제 설명

문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

### 제한 사항

- 1 ≤ indices의 길이 < my_string의 길이 ≤ 100
- my_string은 영소문자로만 이루어져 있습니다
- 0 ≤ indices의 원소 < my_string의 길이
- indices의 원소는 모두 서로 다릅니다.

### 입출력 예

| my_string             | indices                      | result        |
| --------------------- | ---------------------------- | ------------- |
| "apporoograpemmemprs" | [1, 16, 6, 15, 0, 10, 11, 3] | "programmers" |
