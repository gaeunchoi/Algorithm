import sys
from collections import Counter

N, K = map(int, input().split())
lines = list(sys.stdin.readline().rstrip())
# print(lines)

pick_items = [False] * N

for i in range(N):
    if lines[i] == 'P':
        for j in range(i-K, i+K+1):
            if i == j or j < 0 or j >= N:
                continue
            if lines[j] == 'H' and not pick_items[j]:
                pick_items[j] = True
                break

result = 0
for i in pick_items:
    if i:
        result += 1

print(result)