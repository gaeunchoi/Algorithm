for tc in range(1, 11):
    l = int(input())
    words = [list(map(str, input().rstrip())) for _ in range(8)]
    result = []

    for i in range(8):
        for j in range(8):
            if j + l <= 8:
                r = words[i][j : j + l]
                if r == r[::-1]:
                    # result += 1
                    result.append(r)
            c = []
            if i + l <= 8:
                for k in range(i, i+l):
                    c.append(words[k][j])
                if c == c[::-1]:
                    # result += 1
                    result.append(c)

    print(f'#{tc} {len(result)}')