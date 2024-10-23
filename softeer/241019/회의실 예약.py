import sys

N, M = map(int, input().split())

rooms = {}
for i in range(N):
    name = input()
    rooms[name] = [0] * 18

for i in range(M):
    name, start, end = input().split()
    start = int(start)
    end = int(end)
    for j in range(start, end):
        rooms[name][j] = 1

rooms = sorted(rooms.items())

for i in range(N):
    current = 1
    temp = []
    for j in range(9, 18):
        if current == 1 and rooms[i][1][j] == 0:
            sTime = j
            current = 0
        elif current == 0 and rooms[i][1][j] == 1:
            fTime = j
            current = 1
            temp.append([sTime, fTime])

    if current == 0:
        temp.append([sTime, 18])

    print(f"Room {rooms[i][0]}:")
    if len(temp) == 0:
        print("Not available")
    else:
        print(len(temp), "available:")
        for j in range(len(temp)):
            print(f'{temp[j][0]:02d}-{temp[j][1]}')
    if i != N-1:
        print("-----")

