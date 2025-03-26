def convertTime(t):
    h, m = divmod(t, 100)
    return 60 * h + m

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        day = startday - 1
        targetTime = convertTime(schedules[i])

        for time in timelogs[i]:
            # 주말 만나면 넘기기
            if day in [5, 6]:
                day = (day+1)%7
                continue

            t = convertTime(time)

            # 지각 체크
            if t > targetTime + 10:
                break
            else:
                day += 1 

        else:
            answer += 1

    return answer