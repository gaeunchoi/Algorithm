import sys

N = int(input())

min_y_val = 1001
pos = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if y < min_y_val:
        min_y_val = y
        pos = [x, y]
    
print(*pos)