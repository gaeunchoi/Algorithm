n = int(input())

F = list(map(int, input().split()))
F.sort()

max_val = max(F[0]*F[1], F[n-2]*F[n-1])
print(max_val)