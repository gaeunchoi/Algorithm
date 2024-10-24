import sys

N, M = map(int, input().split())

rooms = {}
result = {}

for _ in range(N):
    name = sys.stdin.readline().rstrip()
    rooms[name] = []
    result[name] = []

rooms = dict(sorted(rooms.items()))
result = dict(sorted(result.items()))

for i in range(M):
    r, s, t = sys.stdin.readline().split()
    rooms[r].append([int(s), int(t)])
    rooms[r] = sorted(rooms[r], key=lambda x: x[0])

for room, times in rooms.items():
    # 회의실 예약이 없으면 9시부터 18시까지 이용 가능
    if len(times) == 0:
            result[room].append([9, 18])
    # 회의실 예약이 1개면, 그 앞뒤로 가능한 시간으로 만들어주기
    elif len(times) == 1:
            if times[0][0] > 9:
                result[room].append([9, times[0][0]])
            if times[0][1] < 18:
                result[room].append([times[0][1], 18])
    # 그 외의 예약이 다수인 경우
    else:
        for i in range(len(times)):
            if i == 0:
                if times[i][0] > 9:
                    result[room].append([9, times[i][0]])
                else:
                    continue
            else:
                if times[i-1][1] != times[i][0]:
                    result[room].append([times[i-1][1], times[i][0]])
                
                if i == (len(times)-1) and times[i][1] < 18:
                    result[room].append([times[i][1], 18])

result_list = list(result.items())
for room, times in result_list:
    print('Room ' + room + ':')
    if len(times) == 0:
        print('Not available')
    else:
        print(str(len(times)) + ' available:')
        for time in times:
            print(f'{time[0]:02d}-{time[1]}')
    if room != result_list[-1][0]:
        print('-----')
    