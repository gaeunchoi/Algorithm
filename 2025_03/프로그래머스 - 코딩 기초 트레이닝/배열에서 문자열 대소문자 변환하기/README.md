# [프로그래머스 코딩 기초 트레이닝] 배열에서 문자열 대소문자 변환하기

### 성능 요약

메모리 | 33.3MB  
시간 | 0.04ms

### 분류

문자열

### 제출 일자

2025-03-06 16:17:40

### 문제 설명

문자열 배열 strArr가 주어집니다. 모든 원소가 알파벳으로만 이루어져 있을 때, 배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성해 주세요.

### 제한 사항

- 1 ≤ strArr ≤ 20
  - 1 ≤ strArr의 원소의 길이 ≤ 20
  - strArr의 원소는 알파벳으로 이루어진 문자열 입니다.

### 입출력 예

| strArr                    | result                    |
| ------------------------- | ------------------------- |
| ["AAA","BBB","CCC","DDD"] | ["aaa","BBB","ccc","DDD"] |
| ["aBc","AbC"]             | ["abc","ABC"]             |
