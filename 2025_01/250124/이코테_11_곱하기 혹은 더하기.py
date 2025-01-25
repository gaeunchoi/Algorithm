S = list(map(int, input().rstrip()))

result = S[0]

for i in range(1, len(S)):
    if result <= 1 or S[i] <= 1:
        result += S[i]
    else:
        result *= S[i]
print(result)