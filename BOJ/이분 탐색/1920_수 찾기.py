def binary(target):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == target:
            return True

        if target < a[mid]:
            right = mid-1
        elif target > a[mid]:
            left = mid+1

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
num = list(map(int, input().split()))

for i in range(m):
    if binary(num[i]):
        print(1)
    else:
        print(0)
