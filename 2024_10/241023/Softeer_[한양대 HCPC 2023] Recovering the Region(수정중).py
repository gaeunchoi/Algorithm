import sys
from collections import deque

N = int(input())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [[-1] * N for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(x, y, num):
    q = deque()
    q.append([x, y])

    num_list = [i for i in range(1, N + 1)]

    while q:
        cx, cy = q.popleft()

        if len(num_list) == 0:
            break

        if maps[cx][cy] in num_list:
            result[cx][cy] = num
            num_list.remove(maps[cx][cy])

        for dx, dy in direction:
            mx, my = cx+dx, cy+dy
            if 0 <= mx < N and 0 <= my < N:
                if result[mx][my] == -1 and maps[mx][my] in num_list:
                    result[mx][my] = num
                    q.append([mx, my])
                    num_list.remove(maps[mx][my])

for i in range(N):
    num  = i+1
    for j in range(N):
        if result[i][j] == -1:
            BFS(i, j, num)
        else:
            num += 1

for i in range(N):
    print(*result[i])