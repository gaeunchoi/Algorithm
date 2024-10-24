import math

def solution(r1, r2):
    quarter = 0

    for i in range(1, r2+1):
        for j in range(0, r2+1):
            if r1 <= math.sqrt(pow(i, 2) + pow(j, 2)) <= r2:
                quarter += 1

    answer = quarter * 4
    return answer

print(solution(2, 3))
print(solution(1, 3))