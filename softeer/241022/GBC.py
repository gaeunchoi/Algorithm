import sys

N, M = map(int, input().split())

total = 0
max_v = 0
standard = [0 for i in range(101)]
test = [0 for i in range(101)]

for i in range(N):
    d, v = map(int, sys.stdin.readline().split())
    for j in range(total, total + d):
        standard[j] = v
    total += d

total = 0
for i in range(M):
    d, v = map(int, sys.stdin.readline().split())
    for j in range(total, total + d):
        max_v = max(max_v, v - standard[j])
    total += d

print(max_v)

