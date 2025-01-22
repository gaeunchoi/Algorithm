N = int(input())
order = list(map(str, input().split()))

directs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
directs_str = ['L', 'U', 'R', 'D']

cx, cy = 0, 0

for i in range(len(order)):
    dx, dy = directs[directs_str.index(order[i])]
    mx, my = cx + dx, cy + dy
    if mx < 0 or mx >= N or my < 0 or my >= N:
        continue
    else:
        cx, cy = mx, my

print(cy+1, cx+1)