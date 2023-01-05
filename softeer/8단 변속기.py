nums = list(map(int, input().split()))

asc = sorted(nums)
des = sorted(nums, reverse=True)

if asc == nums:
    print("ascending")
elif des == nums:
    print("descending")
else:
    print("mixed")