T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0

    for i in range(N):
        for j in range(N):
            for k in range(1, N+1):
                if result > k:
                    break
                tmp = 0
                if i + k <= N and j + k <= N:
                    Asplit, Bsplit = A[i:i+k], B[j:j+k]
                    for l in range(k):
                        tmp += 1 if Asplit[l] == Bsplit[l] else 0

                    result = max(tmp, result)

    print(f'#{tc} {result}')