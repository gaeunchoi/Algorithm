import itertools

N, M, K = map(int, input().split())
rails = list(map(int, input().split()))

permu_rails = list(itertools.permutations(rails, N))

results = []
for i in range(len(permu_rails)):
    result = 0
    idx = 0
    for j in range(K):
        weight = 0
        while True:
            weight += permu_rails[i][idx]
            idx = (idx+1) % N

            if weight + permu_rails[i][idx] > M:
                break

        result += weight
    results.append(result)

print(min(results))