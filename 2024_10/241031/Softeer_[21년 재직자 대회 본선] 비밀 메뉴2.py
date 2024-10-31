import sys

N, M, K = map(int, sys.stdin.readline().split())
menu = list(map(int, sys.stdin.readline().split()))
button = list(map(int, sys.stdin.readline().split()))
C = [[0] * M for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if menu[i] == button[j]:
            if i == 0 or j == 0:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + 1
            result = max(result, C[i][j])

print(C)

print(result)