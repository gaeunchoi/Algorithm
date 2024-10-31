import sys

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

n, m = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

targets = []
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    targets.append([x - 1, y - 1])


def dfs(points, depth):
    if depth == m:
        result.append(points)
        return

    if points[-1] == targets[depth]:
        dfs(points, depth + 1)
        return

    x, y = points[-1][0], points[-1][1]
    for dx, dy in directions:
        mx, my = x + dx, y + dy

        if (mx < 0 or n <= mx or my < 0 or n <= my) or maps[mx][my] == 1:
            continue

        if [mx, my] not in points:
            # print(points + [[mx, my]])
            dfs(points + [[mx, my]], depth)


result = []
dfs([targets[0]], 0)

# print(*result)
print(len(result))