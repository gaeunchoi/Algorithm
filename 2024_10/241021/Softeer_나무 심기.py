n = int(input())

F = list(map(int, input().split()))
F.sort()

print(max(F[0]*F[1], F[n-2]*F[n-1]))