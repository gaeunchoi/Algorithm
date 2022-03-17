import sys

N = int(sys.stdin.readline())

keyword = []
for _ in range(N):
    keyword.append(str(sys.stdin.readline().strip()))

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 0
    word = str(sys.stdin.readline().strip())

    for j in keyword:
        if j.startswith(word):
            cnt += 1

    print(cnt)
