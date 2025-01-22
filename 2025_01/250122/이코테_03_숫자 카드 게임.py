n, m = map(int, input().split())

data = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    data.append(min(tmp))

print(max(data))