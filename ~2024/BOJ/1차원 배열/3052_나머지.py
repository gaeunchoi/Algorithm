data = []

for i in range(10):
    n = int(input())
    data.append(n % 42)

result = len(list(set(data)))
print(result)

