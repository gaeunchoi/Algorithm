import sys

N, K = map(int, input().split())

scores = list(map(int, input().split()))
ran = []

for _ in range(K):
    start, end = map(int, sys.stdin.readline().split())
    total_score = sum(scores[start-1: end])
    total_stu = end - start + 1
    print('%.2f' % (total_score/total_stu))