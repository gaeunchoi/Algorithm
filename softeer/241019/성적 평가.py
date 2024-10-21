# 시간초과 해결 x
import sys

n = int(sys.stdin.readline())

scores = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
total_score = [x+y+z for x, y, z in zip(scores[0], scores[1], scores[2])]

for score in scores:
    ranks = ''
    for i in range(n):
        cnt = len(list(filter(lambda num: num > score[i], score)))
        ranks += (str(cnt+1) + " ")
        total_score[i] += score[i]
    print(ranks)

for score in total_score:
    print(len(list(filter(lambda num: num > score, total_score)))+1, end=' ')

# for _ in range(3):
#     scores = list(map(int, sys.stdin.readline().split()))
#     rank = ""
#
#     for i in range(len(scores)):
#         cnt = len(list(filter(lambda num: num > scores[i], scores)))
#         rank += (str(cnt+1) + " ")
#         total_score[i] += scores[i]
#     print(rank)
#
# for i in range(len(total_score)):
#     cnt = len(list(filter(lambda num: num > total_score[i], total_score)))
#     print(cnt+1, end = " ")

