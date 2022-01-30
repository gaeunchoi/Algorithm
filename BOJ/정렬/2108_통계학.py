import sys
from collections import Counter
N = int(sys.stdin.readline())

def most_common_num(nums):
    if len(nums) == 0:
        return None

    return Counter(nums).most_common(n=1)[0][0]

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

print(round(sum(nums)/N))

nums.sort()
print(nums[int(N/2)])

# 미완성
print(most_common_num(nums))
