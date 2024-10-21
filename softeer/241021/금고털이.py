W, N = map(int, input().split())

jewelry = []
for i in range(N):
    jewelry.append(list(map(int, input().split())))

jewelry.sort(key = lambda x: x[1], reverse = True)

result = 0
for weight, price in jewelry:
    if weight < W:
        result += weight * price
        W -= weight
    else:
        result += W * price
        break

print(result) 
