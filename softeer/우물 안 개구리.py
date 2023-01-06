import sys
n, m = map(int, sys.stdin.readline().split())

W = list(map(int, sys.stdin.readline().split()))

users = [True for _ in range(n)]

for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))

    if W[a-1] < W[b-1]:
        users[a-1] = False
    elif W[a-1] > W[b-1]:
        users[b-1] = False
    else:
        users[a-1] = users[b-1] = False

answer = 0
for user in users:
    if user:
        answer += 1

print(answer)