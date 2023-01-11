maxnum, maxi, maxj = -1, 0, 0

for i in range(9):
    nums = list(map(int, input().split()))
    tmp = max(nums)
    if maxnum < tmp:
        maxnum, maxi, maxj = tmp, i+1, nums.index(maxnum) + 1

print(maxnum)
print(maxi, maxj)