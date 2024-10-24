N = int(input())
for _ in range(N):
    S, T = input().split()
    for i in range(len(S)):
        if S[i] == 'x' or S[i] == 'X':
            print(T[i].upper(), end = '')