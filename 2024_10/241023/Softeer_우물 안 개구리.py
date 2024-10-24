import sys

N, M = map(int, input().split())
weights = list(map(int, input().split()))
users = [True for _ in range(N)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())

    if weights[A-1] > weights[B-1]:
        users[B-1]  = False
    elif weights[A-1] < weights[B-1]:
        users[A-1] = False
    else:
        users[A-1] = users[B-1] = False

cnt = 0
for user in users:
    if user: cnt += 1

print(cnt)