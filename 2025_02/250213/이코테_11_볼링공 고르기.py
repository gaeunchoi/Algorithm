N, M = map(int, input().split())
weights = list(map(int, input().split()))
cnt = [0] * 11

for i in weights:
    cnt[i] += 1

result = 0
for i in range(1, M):
    N -= cnt[i]
    result += cnt[i] * N

print(result)