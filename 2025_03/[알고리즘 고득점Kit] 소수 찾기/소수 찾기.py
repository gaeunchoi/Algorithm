# 진짜 개개개개개ㅐㅎㄱ스트레스 이^ㅐ기 패고싶네 넌 JS로 못푼다;
# permutations를 이용해서 한 자리수부터 len(numbers) 자리수까지 순열 조합 만들기
# "17" => "1", "7" -> ["1"], ["7"], ["1", "7"], ["7", "1"]
# join으로 숫자 하나로 만들기 => 1, 7, 17, 71
# 소수 판별 거치고 중복 안되게 체크해서 answer에 넣기

# for-else 구문 사용
from itertools import permutations

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        for j in permutations(list(numbers), i):
            permu_num = int(''.join(j))

            for k in range(2, int(permu_num**0.5)+1):
                if permu_num % k == 0:
                    break
            else:
                if permu_num not in answer and permu_num >= 2:
                  answer.append(permu_num)
    return len(answer)

print(solution("17"))
print(solution("011"))


# 에라토스테네서의 체 -> set으로 이용한 풀이
# 이걸 어케 생각하농 ...
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)