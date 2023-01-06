import sys

n = int(sys.stdin.readline())

total_score = [0 for _ in range(n)]

for _ in range(3):
    scores = list(map(int, sys.stdin.readline().split()))
    rank = [0 for _ in range(n)]

    for i in range(len(scores)):
        # cnt = 0
        cnt = len(list(filter(lambda  num: num > scores[i], scores)))
        rank[i] = cnt+1
        total_score[i] += scores[i]
        print(rank[i], end=" ")
    print()

for i in range(len(total_score)):
    cnt = len(list(filter(lambda num: num > total_score[i], total_score)))
    print(cnt+1, end = " ")

# 시간초과 뚫기