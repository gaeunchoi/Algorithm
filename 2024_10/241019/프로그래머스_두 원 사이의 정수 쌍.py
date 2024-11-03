import math

def solution(r1, r2):
    quarter = 0

    for i in range(1, r2+1):
        s = math.ceil(math.sqrt(r1 ** 2 - i ** 2)) if i < r1 else 0
        
        e = int(math.sqrt(r2 ** 2 - i ** 2))
        quarter += e - s + 1

    return 4 * quarter

print(solution(2, 3))
print(solution(1, 3))