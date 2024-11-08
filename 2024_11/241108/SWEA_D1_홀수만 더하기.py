T = int(input())

for test_case in range(1, T + 1):
    result = 0
    nums = list(map(int, input().split()))
    for element in nums:
        result += element if element % 2 == 1 else 0
    print(f'#{test_case} {result}')