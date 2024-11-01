import sys

N = int(input())
A, B = [[0] * (N + 1) for _ in range(2)]
movetime = [[0, 0] for _ in range(N + 1)]

for i in range(1, N):
    if i <= N:
        a, b, a2b, b2a = map(int, sys.stdin.readline().split())
        movetime[i] = [a2b, b2a]

        # Ai로 올 수 있는 경우는 Bi-1 -> Ai, Ai-1 -> Ai
        total_a2a = A[i - 1] + a
        total_b2a = B[i - 1] + movetime[i - 1][1] + a
        A[i] = min(total_a2a, total_b2a)

        # Bi로 올 수 있는 경우는 Ai-1 -> Bi, Bi-1 -> Bi
        total_b2b = B[i - 1] + b
        total_a2b = A[i - 1] + movetime[i - 1][0] + b
        B[i] = min(total_b2b, total_a2b)

a, b = map(int, sys.stdin.readline().split())
# Ai로 올 수 있는 경우는 Bi-1 -> Ai, Ai-1 -> Ai
total_a2a = A[N - 1] + a
total_b2a = B[N - 1] + movetime[N - 1][1] + a
A[N] = min(total_a2a, total_b2a)

# Bi로 올 수 있는 경우는 Ai-1 -> Bi, Bi-1 -> Bi
total_b2b = B[N - 1] + b
total_a2b = A[N - 1] + movetime[N - 1][0] + b
B[N] = min(total_b2b, total_a2b)

print(min(A[N], B[N]))
