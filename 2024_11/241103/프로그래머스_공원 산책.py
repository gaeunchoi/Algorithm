def solution(park, routes):
    answer = []
    H, W = len(park), len(park[0])
    
    cx, cy = 0, 0
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                cx, cy = i, j

    for route in routes:
        direction, distance = map(str, route.split())
        mx, my = cx, cy
        if direction == 'N':
            mx = cx - int(distance)
        elif direction == 'S':
            mx = cx + int(distance)
        elif direction == 'W':
            my = cy - int(distance)
        else:
            my = cy + int(distance)
            
        if not (mx < 0 and H <= mx and my < 0 and W <= my):
            for i in range(min(cx, mx), max(cx, mx)+1):
                for j in range(min(cy, my), max(cx, mx)+1):
                    if park[i][j] == 'S':
                        break
            print('move pos:', mx, my)
            cx, cy = mx, my
            
    return [cx, cy]