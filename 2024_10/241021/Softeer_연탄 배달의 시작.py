n = int(input())

pos = list(map(int, input().split()))

distance = []
for i in range(1, n):
    distance.append(pos[i] - pos[i-1])

print(distance.count(min(distance)))