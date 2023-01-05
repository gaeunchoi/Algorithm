import  sys

W, N = map(int, sys.stdin.readline().split())

jewelry = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
jewelry.sort(key=lambda x: x[1], reverse=True)

total = 0
for weight, price in jewelry:
    if weight < W:
        total += weight * price
        W -= weight

    else:
        total += W * price
        break

print(total)