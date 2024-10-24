N = int(input())
stones = list(map(int, input().split()))

result = [1] * N

for i in range(1, N):
    for j in range(i):
        if stones[i] > stones[j]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))