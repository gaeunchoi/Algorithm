# [프로그래머스 Lv.1] 문자열 내 p와 y의 개수

### 성능 요약

- py  
  메모리 | 9.06MB  
  시간 | 0.01ms

- js  
  메모리 | 33.4MB  
  시간 | 0.07ms

### 분류

프로그래머스 연습문제 Lv.1

### 제출 일자

2025-03-18 20:45:49

### 문제 설명

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

### 제한 사항

- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.

### 입출력 예

| s         | return |
| --------- | ------ |
| "pPoooyY" | true   |
| "Pyy"     | false  |
