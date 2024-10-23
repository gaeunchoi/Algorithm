N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0

    if graph[x][y]:
        graph[x][y] = 0

        cnt = 1
        cnt += DFS(x-1, y)
        cnt += DFS(x, y-1)
        cnt += DFS(x+1, y)
        cnt += DFS(x, y+1)
        return cnt

    return 0

result = []
for i in range(N):
    for j in range(N):
        tmp = DFS(i, j)
        if tmp:
            result.append(tmp)

result.sort()
print(len(result))
for i in result:
    print(i)