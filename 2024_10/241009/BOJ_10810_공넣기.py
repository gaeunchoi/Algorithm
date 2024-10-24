n, m = map(int, input().split())
basket = [0 for i in range(n)]

for x in range(m):
    i, j, k = map(int, input().split())
    for y in range (i-1, j):
        basket[y] = k

for x in basket:
    print(str(x), end = " ")