N, M = map(int, input().split())

cx, cy, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

directs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0

while True:
    