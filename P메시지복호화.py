a, b = map(int, input().split())

T = str(input())

alpha = [0 for _ in range(26)]
for i in range(26):
    alpha[i] = chr(((a*i + b) % 26) + 97)

for i in range(len(T)):
    for j in range(26):
        if T[i] == alpha[j]:
            print(chr(j + 97))