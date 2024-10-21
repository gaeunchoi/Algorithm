n = int(input())
r_list = list(map(int, input().split()))
r_list.sort()

result = 0
for i in range(2, max(r_list) + 1):
    cnt = 0
    for j in range(n):
        if r_list[j] % i == 0:
            cnt += 1
    result = max(result, cnt)

print(result)