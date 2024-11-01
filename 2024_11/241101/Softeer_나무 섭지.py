import sys
from collections import deque

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
n, m = map(int, input().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

def bfs(start, is_namwoo):
    q = deque()
    visited = [[-1] * m for _ in range(n)]

    for x, y in start:
        q.append([x, y, 0])
        visited[x][y] = 0

    while q:
        x, y, time = q.popleft()

        # 남우가 목적지에 도착하면 걸린 시간만 리턴
        if is_namwoo and maps[x][y] == 'D':
            return time

        # 남우 / 귀신이 이동하면 거리 증가해서 방문 기록
        for dx, dy in directions:
            mx, my = x + dx, y + dy
            if 0 <= mx < n and 0 <= my < m and visited[mx][my] == -1:
                if is_namwoo:
                    if maps[mx][my] != '#':
                        q.append([mx, my, time + 1])
                        visited[mx][my] = time + 1
                else:
                    q.append([mx, my, time + 1])
                    visited[mx][my] = time + 1

    return visited if not is_namwoo else -1

N_start = []
G_start = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'N':
            N_start.append([i, j])
        elif maps[i][j] == 'G':
            G_start.append([i, j])

G_time = bfs(G_start, False)
N_time = bfs(N_start, True)
# print(G_time,N_time)

if N_time != -1:
    escape = True
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'D' and G_time[i][j] != -1 and G_time[i][j] <= N_time:
                escape = False
                break
        if not escape:
            print('No')
            sys.exit()
    print('Yes')

else:
    print('No')