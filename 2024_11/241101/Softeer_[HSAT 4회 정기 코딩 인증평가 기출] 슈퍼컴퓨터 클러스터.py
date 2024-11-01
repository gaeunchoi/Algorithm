import sys
sys.setrecursionlimit(10**8)

def check_cost(mid):
    cost = 0
    for com in coms:
        if mid > com:
            cost += (mid - com) ** 2

    if cost <= B:
        return True
    else:
        return False

def binary_search(left, right):
    if left == right:
        return left
    mid = (left + right + 1) // 2
    if check_cost(mid):
        return binary_search(mid, right)
    else:
        return binary_search(left, mid-1)


N, B = map(int, input().split())
coms = sorted(list(map(int, input().split())))
result = binary_search(coms[0], 2 * 10 ** 9)
print(result)