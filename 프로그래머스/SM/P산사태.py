import sys

N, Q = map(int, sys.stdin.readline().split())

size_limit = []
for _ in range(N-1):
    size_limit.append(int(sys.stdin.readline))

for _ in range(Q):
    i, k, s = map(int, sys.stdin.readline())
