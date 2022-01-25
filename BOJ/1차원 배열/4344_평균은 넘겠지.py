import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(n):
    score = list(map(int, sys.stdin.readline().split()))
    avg = sum(score[1:]) // score[0]
    for j in score[1:]:
        if avg < j:
            cnt += 1
    print("%.3f%%" % ((cnt/score[0]) * 100))
    cnt = 0