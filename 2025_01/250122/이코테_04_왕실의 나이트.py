current = input()
c, r = int(ord(current[0])) - int(ord('a')) + 1, int(current[1])

directs = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]

result = 0
for dr, dc in directs:
    mr, mc = r + dr, c + dc
    if 1 <= mr <= 8 and 1 <= mc <= 8:
        result += 1

print(result)
