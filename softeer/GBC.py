import sys
n, m = map(int, input().split())

# 각 구간별 구간의 길이와 제한속도 설정
height = 0
limit = [0 for i in range(101)]
for i in range(n):      # 제한
    length, limitSpeed = map(int, sys.stdin.readline().split())
    for j in range(height + 1, height + length + 1):        # 해당 구간에 제한속도 설정
        limit[j] = limitSpeed
    height += length

# 각 구간별 구간의 테스트 길이와 제한속도 입력
speed = [0 for i in range(101)]
height = 0
for i in range(m):
    length, limitSpeed = map(int, sys.stdin.readline().split())
    for j in range(height + 1, height+ length + 1):
        speed[j] = limitSpeed
    height += length

maxSpeed = 0
for i in range(101):
    maxSpeed = max(maxSpeed, speed[i] - limit[i])       # 테스트 속도가 제한속도보다 클 때마다 max 갱신

print(maxSpeed)