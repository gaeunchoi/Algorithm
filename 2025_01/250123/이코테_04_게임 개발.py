N, M = map(int, input().split())

cx, cy, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

# 방문 맵 생성 후 현재위치 방문 표시
visited = [[False] * M for _ in range(N)]
visited[cx][cy] = True

# 북 동 남 서
directs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

cnt = 1
rotate_cnt = 0

while True:
    # 왼쪽으로 회전
    d -= 1
    if d < 0:
        d = 3

    mx, my = cx + directs[d][0], cy + directs[d][1]
    if visited[mx][my] == False and data[mx][my] == 0:      # 방문하지 않았고 이동할 위치가 육지라면
        visited[mx][my] = True
        cnt += 1
        rotate_cnt = 0
        cx, cy = mx, my
        continue
    else:
        rotate_cnt += 1

    if rotate_cnt == 4:
        mx, my = cx - directs[d][0], cy - directs[d][1]
        if data[mx][my] == 0:
            cx, cy = mx, my
        else:
            break
        rotate_cnt = 0

print(cnt)