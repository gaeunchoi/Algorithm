import sys

n, q = map(int, input().split())
oils = list(map(int, input().split()))
oils.sort()

result = {}
for i in range(n):
    result[oils[i]] = i * (n - i - 1)

for _ in range(q):
    m = int(sys.stdin.readline().rstrip())
    if m not in result.keys():
        print(0)
    else:
        print(result[m])