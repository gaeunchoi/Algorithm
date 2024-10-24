# 다 초로 바꾸고 각도 계산 ??
# 1시간 -> 60분 -> 3600초
# 1분 -> 60초

# 시침은 360/12 = 1시간에 30도 = 1분에 0.5도 = 1초에 1/120도
# 분침은 360/60 = 1분에 6도 = 1초에 0.1도
# 초침은 360/60 = 1초에 6도
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start_time, end_time = h1 * 3600 + m1 * 60 + s1, h2 * 3600 + m2 * 60 + s2

    # 0시 0분 0초나 12시 00분 00초는 무조건 겹친다
    if start_time == 0 or start_time == 12 * 3600:
        answer += 1

    while start_time < end_time:
        h_angle = start_time / 120 % 360
        m_angle = start_time / 10 % 360
        s_angle = start_time * 6 % 360

        next_h_angle = 360 if (start_time + 1) / 120 % 360 == 0 else (start_time + 1) / 120 % 360
        next_m_angle = 360 if (start_time + 1) / 10 % 360 == 0 else (start_time + 1) / 10 % 360
        next_s_angle = 360 if (start_time + 1) * 6 % 360 == 0 else (start_time + 1) * 6 % 360

        # 1초후에 초침이 시침을 넘어가면
        if s_angle < h_angle and next_h_angle <= next_s_angle:
            answer += 1

        # 1초 후에 초침이 분침을 넘어가면
        if s_angle < m_angle and next_m_angle <= next_s_angle:
            answer += 1

        if next_s_angle == next_m_angle == next_h_angle:
            answer -= 1

        start_time += 1
    return answer


print(solution(0, 5, 30, 0, 7, 0))
print(solution(12, 0, 0, 12, 0, 30))
print(solution(0, 6, 1, 0, 6, 6))
print(solution(11, 59, 30, 12, 0, 0))
print(solution(11, 58, 59, 11, 59, 0))
print(solution(1, 5, 5, 1, 5, 6))
print(solution(0, 0, 0, 23, 59, 59))