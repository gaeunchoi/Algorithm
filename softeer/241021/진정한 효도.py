min_val = 3

pos = [[] for _ in range(3)]
for i in range(3):
    pos[i] = list(map(int, input().split()))

for row in pos:
    x, y, z = row
    if x == y == z:
        min_val = 0
        break
    else:
        pivot_val = (x + y + z) - min(row) - max(row)
        min_val = min(min_val, sum(list(map(lambda k: abs(k-pivot_val), row))))

for j in range(3):
    x, y, z = pos[0][j], pos[1][j], pos[2][j]
    if x == y == z:
        min_val = 0
        break
    else:
        col = [x, y, z]
        pivot_val = (x + y + z) - min(row) - max(row)
        min_val = min(min_val, sum(list(map(lambda k: abs(k-pivot_val), col))))

print(min_val)