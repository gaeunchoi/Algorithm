def binary(target):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if card[mid] == target:
            return target
        if target < card[mid]:
            right = mid-1
        elif target > card[mid]:
            left = mid+1


n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
num = list(map(int, input().split()))

