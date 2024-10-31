import sys
N = int(input())
nums = list(map(int, input().split()))
result = 0

# for i in range(len(nums)-2):
#     for j in range(i+1, len(nums)-1):
#         if i < j and nums[i] < nums[j]:
#             for k in range(j+1, len(nums)):
#                 if j < k and nums[k] < nums[i]:
#                     result += 1

for i in range(N):
    able = 0
    for j in range(i+1, N):
        if nums[i] < nums[j]:
            able += 1
        elif nums[i] > nums[j]:
            result += able

print(result)