T = int(input())

for tc in range(1, T+1):
    N = int(input())

    nums = list(map(int, input().split()))
    abs_nums = [abs(x) for x in nums]

    distance = min(nums)
    cnt = nums.count(distance)

    print(f'#{tc} {distance} {cnt}')