import sys
from itertools import permutations

n, m = map(int, input().split())

fruits = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
position = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
visited = [[False] * n for _ in range(n)]

def DFS(x, y, fruit, iter, path):
    global max_fruits, max_path
    visited[x][y] = True
    fruit += fruits[x][y]
    path.append((x, y))

    if iter == 3:
        if max_fruits < fruit:
            max_fruits = fruit
            max_path = path[:]
        return

    for dx, dy in direction:
        mx, my = x + dx, y + dy
        if (0 <= mx < n and 0 <= my < n) and not visited[mx][my] and not (mx, my) in total_path:
            DFS(mx, my, fruit, iter+1, path)
            visited[mx][my] = False
            path.pop()


permu_pos = list(permutations(position, m))
result = 0

for pos in permu_pos:
    total_fruits = 0
    total_path = []

    for x, y in pos:
        max_fruits, max_path = 0, []
        DFS(x-1, y-1, 0, 0, [])
        total_fruits += max_fruits
        total_path += max_path
    result = max(result, total_fruits)

print(result)