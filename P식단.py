
import itertools

N = int(input())

cal = list(map(int,input().split()))

cnt = 0

foodlist = list(itertools.combinations(cal, 3))

for value in foodlist:
    if 2000 <= sum(value) <= 2500:
        cnt += 1

print(cnt)