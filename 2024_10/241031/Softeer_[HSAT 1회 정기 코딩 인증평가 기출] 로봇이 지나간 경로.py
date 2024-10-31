import sys
from collections import deque

H, W = map(int, input().split())
maps = [list(sys.stdin.readline()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]
num_directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
directions = ['^', '<', 'v', '>']
ans = []


def check_map(x, y):
    cnt = 0
    for i in range(len(num_directions)):
        dx, dy = num_directions[i][0], num_directions[i][1]
        mx, my = x + dx, y + dy
        if 0 <= mx < H and 0 <= my < W and maps[mx][my] == '#':
            start = directions[i]
            cnt += 1

    if cnt > 1:
        return False

    return start


def bfs(x, y):
    path = deque([])
    q = deque([[x, y]])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for i in range(len(num_directions)):
            dx, dy = num_directions[i][0], num_directions[i][1]
            mx, my = cx + dx, cy + dy

            if 0 <= mx < H and 0 <= my < W and maps[mx][my] == '#' and not visited[mx][my]:
                visited[mx][my] = True
                path.append(directions[i])
                q.append([mx, my])
    return path


for i in range(H):
    for j in range(W):
        if maps[i][j] == '#' and check_map(i, j):
            path = bfs(i, j)
            print(i + 1, j + 1)
            print(path[0])

            current = path.popleft()

            cnt = 1
            for next in path:
                if current == next:
                    cnt += 1
                    current = next

                    if cnt % 2 == 0:
                        ans.append("A")
                        cnt = 0

                else:
                    if directions[directions.index(current) - 1] == next:
                        ans.append('R')
                    else:
                        ans.append('L')
                    current = next
                    cnt = 1

            for i in ans:
                print(i, end="")

            sys.exit()

