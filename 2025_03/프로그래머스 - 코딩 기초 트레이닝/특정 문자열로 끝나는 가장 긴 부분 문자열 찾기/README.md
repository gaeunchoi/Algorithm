# [프로그래머스 코딩 기초 트레이닝] 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

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

2025-03-17 13:20:24

### 문제 설명

문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

### 제한 사항

- 5 ≤ myString ≤ 20
- 1 ≤ pat ≤ 5
  - pat은 반드시 myString의 부분 문자열로 주어집니다.
- myString과 pat에 등장하는 알파벳은 대문자와 소문자를 구분합니다.

### 입출력 예

| myString   | pat  | result     |
| ---------- | ---- | ---------- |
| "AbCdEFG"  | "dE" | "AbCdE"    |
| "AAAAaaaa" | "a"  | "AAAAaaaa" |
