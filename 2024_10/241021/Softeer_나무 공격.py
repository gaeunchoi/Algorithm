import sys

result = 0

n, m = map(int, input().split())

pos = [[] for _ in range(n)]

for i in range(n):
    pos[i] = list(map(int, input().split()))
    result += sum(pos[i])

for i in range(2):
    sl, el = map(int, input().split())

    for j in range(sl-1, el):
        for k in range(m):
            if pos[j][k] == 1:
                result -= 1
                pos[j][k] = 0
                break
  
print(result)
