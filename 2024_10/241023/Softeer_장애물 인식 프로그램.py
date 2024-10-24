import sys

N = int(input())
maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
print(maps)

def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0

    if maps[x][y]:
        maps[x][y] = 0

        cnt = 1
        cnt += DFS(x-1, y)
        cnt += DFS(x+1, y)
        cnt += DFS(x, y-1)
        cnt += DFS(x, y+1)
        return cnt

    return 0

result = []
for i in range(N):
    for j in range(N):
        block = DFS(i, j)
        if block:
            result.append(block)

result.sort()
print(len(result))
for block in result:
    print(block)