# Runtime Error 해결 x
import sys
import itertools

n, m, k = map(int, sys.stdin.readline().split())

buttons = list(map(int, sys.stdin.readline().split()))
push = list(map(int, sys.stdin.readline().split()))

permu_buttons = []
permu_push = []

if n < m:
    for i in range(n):
        for j in range(i+1, n+1):
            permu_buttons.append([buttons[i:j]])

    for i in range(m):
        if i >= m-n+1:  # 예외
            for j in range(i+1, m+1):
                permu_push.append([push[i:j]])
        else:
            for j in range(i+1, n+i+1):
                permu_push.append([push[i:j]])
else:
    for i in range(m):
        for j in range(i+1, m+1):
            permu_push.append([push[i:j]])

    for i in range(n):
        if i >= n-m+1:
            for j in range(i+1, n+1):
                permu_buttons.append([buttons[i:j]])
        else:
            for j in range(i+1, m+i+1):
                permu_buttons.append([buttons[i:j]])

permu_buttons = list(itertools.chain(*permu_buttons))
permu_push = list(itertools.chain(*permu_push))

# print(permu_buttons)
# print(permu_push)

result = []
for i in permu_buttons:
    for j in permu_push:
        if i == j and j not in result:
            result.append(i)

# print(result)
if len(result) == 0:
    print("0")
else:
    print(len(max(result, key = len)))
