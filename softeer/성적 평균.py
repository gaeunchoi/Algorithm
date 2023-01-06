import sys

n, k = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())

    avg = sum(scores[a-1:b]) / (b-a+1)

    print("%.2f" % avg)