import itertools

n, m, k = map(int, input().split())
rail = list(map(int, input().split()))

permu_rail = list(itertools.permutations(rail, n))

result = []

for i in range(len(permu_rail)):
    ans = 0
    idx = 0
    for j in range(k):
        weight = 0
        while True:
            weight += permu_rail[i][idx]
            idx = (idx+1) % n

            if weight + permu_rail[i][idx] > m:
                break

        ans += weight
    result.append(ans)

print(min(result))
