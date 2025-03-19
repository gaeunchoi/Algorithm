def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            cnt += 1 if i % j == 0 else 0
        answer += i if cnt % 2 == 0 else -i
    return answer


# 제곱수 => 약수의 개수가 홀수개
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        answer += -i if int(i**0.5) == i**0.5 else i
    return answer