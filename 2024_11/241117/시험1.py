T = int(input())

for tc in range(1, T + 1):
    N, D, X = map(int, input().split())
    boxes = list(map(int, input().split()))
    ballcnt = boxes[D - 1]
    cnt, result, idx = 0, 0, D % N

    while True:
        if idx == D-1:
            cnt += 1

        if cnt == ballcnt and idx == X-1:
            result += 1
            break

        result += 1
        idx = (idx + 1) % N

    print(f'#{tc} {result}')