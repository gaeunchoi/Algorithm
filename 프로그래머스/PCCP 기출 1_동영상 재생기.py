def checkOpening(start_m, start_s, end_m, end_s, pos_m, pos_s):
    if ((start_m < pos_m < end_m) or \
        (start_m < pos_m == end_m and pos_s <= end_s) or \
        (start_m == pos_m < end_m and start_s <= pos_s) or \
        (start_m == pos_m == end_m and start_s <= pos_s <= end_s)):
            return end_m, end_s
    else:
        return pos_m, pos_s

def solution(video_len, pos, op_start, op_end, commands):
    video_len_m, video_len_s = map(int, video_len.split(":"))
    pos_m, pos_s = map(int, pos.split(":"))
    start_m, start_s = map(int, op_start.split(":"))
    end_m, end_s = map(int, op_end.split(":"))

    pos_m, pos_s = checkOpening(start_m, start_s, end_m, end_s, pos_m, pos_s)

    for comm in commands:
        # comm이 next인 경우 10초를 더했을 때
        # 1. 비디오 길이를 벗어나는지 체크
        # 2. 비디오 길이 내에 있을때 초가 60초 이상인지 체크
        # 2-1. 이 때 비디오 길이를 넘었을 때도 체크
        # 3. 위 조건에 걸리지 않는 모든 경우는 초만 10초 추가
        if comm == 'next':
            if pos_m == video_len_m and pos_s + 10 >= video_len_s:
                pos_m, pos_s = video_len_m, video_len_s
            elif pos_m < video_len_m and pos_s + 10 >= 60:
                pos_m, pos_s = pos_m + 1, (pos_s + 10) % 60
                if pos_m >= video_len_m and pos_s >= video_len_s:
                    pos_m, pos_s = video_len_m, video_len_s
            else:
                pos_s += 10


        # comm이 prev인 경우 10초를 뺐을 때
        # 1. 비디오 길이를 벗어나는지 체크
        # 2. 비디오 길이 내에 있을때 초가 0초 미만인지 체크
        # 13:00 10 12 50 13:07 10 12:57
        # 3. 위 조건에 걸리지 않는 모든 경우는 초만 10초 추가
        else:
            if pos_m == 0 and pos_s - 10 <= 0:
                pos_m = pos_s = 0
            elif pos_m > 0 and pos_s - 10 < 0:
                pos_m, pos_s = pos_m - 1, 50 + pos_s
            else:
                pos_s -= 10

        pos_m, pos_s = checkOpening(start_m, start_s, end_m, end_s, pos_m, pos_s)

    if pos_m // 10 == 0:
        pos_m = '0' + str(pos_m)
    if pos_s // 10 == 0:
        pos_s = '0' + str(pos_s)

    answer = str(pos_m) + ':' + str(pos_s)
    return answer

print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))

print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))

print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))

print(solution( "30:00", "00:08", "00:00", "00:05", ["prev"]))

print(solution("10:00", "07:05", "01:00", "01:30", ["prev"]))

print(solution( "59:59", "59:45", "00:00", "01:00", ["next"]))

print(solution( "30:00", "29:55", "01:00", "01:30", ["next"]))