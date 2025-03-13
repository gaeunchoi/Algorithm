# 정답 개수가 찍는 패턴 개수보다 길 수도 있으니 나머지 연산으로 반복하게 해야함
# 큰 값이 여러개면 다 result에 추가해야하니 max(score)랑 비교
def solution(answers):
    result = []
    score = [0, 0, 0]
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, answer in enumerate(answers):
        if answer == person1[idx % len(person1)]:
            score[0] += 1
        if answer == person2[idx % len(person2)]:
            score[1] += 1
        if answer == person3[idx % len(person3)]:
            score[2] += 1
    
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result