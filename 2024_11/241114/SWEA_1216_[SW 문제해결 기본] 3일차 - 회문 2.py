for _ in range(1, 11):
    case = int(input())
    words = [list(map(str, input().rstrip())) for _ in range(100)]
    words_zip = list(zip(*words))

    result = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if j + k < 100:
                    r = words[i][j: j + k]
                    c = words_zip[i][j: j + k]
                    if r == r[::-1] or c == c[::-1]:
                        result = max(result, k)
    print(f'#{case} {result}')