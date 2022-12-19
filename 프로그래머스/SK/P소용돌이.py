def solution(n, clockwise):
    num = 0  # 숫자 1, 2, 3, ...

    step = 1  # 증가/감소 크기: 1, -1
    y = 0  # 줄 위치
    x = -1  # 칸 위치 (배열 선두보다 한칸 앞)

    arr = [[0] * n for i in range(n)]  # 2차원 배열 구조

    if clockwise == True:
        while True:
            for _ in range(n-1):  # 몇 칸 진행할까
                num += 1
                x += step
                arr[y][x] = num
            num -= 1

            if num < 1:  # 출력할 게 없으면 종료
                break

            for _ in range(n//2):  # 몇 줄 진행할까
                num += 1
                y += step
                arr[y][x] = num

            step = -step  # 증감 방향을 반대로
    else:
        while True:
            for _ in range(n - 1):  # 몇 칸 진행할까
                num += 1
                x += step
                arr[y][-x] = num
            n -= 1

            if num < 1:  # 출력할 게 없으면 종료
                break

            for _ in range(n // 2):  # 몇 줄 진행할까
                num += 1
                y += step
                arr[y][-x] = num

            step = -step  # 증감 방향을 반대로
    return arr

print(solution(5, True))