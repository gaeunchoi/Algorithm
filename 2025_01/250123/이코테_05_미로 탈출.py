from collections import deque

N, M = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            mx, my = cx + dx, cy + dy
            if not (0 <= mx < N and 0 <= my < M):   # 맵 탈출
                continue
            if data[mx][my] == 0:                   # 괴물 o
                continue
            if data[mx][my] == 1:                   # 괴물 x
                data[mx][my] = data[cx][cy] + 1
                q.append((mx, my))

    return data[N-1][M-1]

print(bfs(0, 0))