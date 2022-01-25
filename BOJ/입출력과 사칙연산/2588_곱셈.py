A = int(input())
B = input()
for digit in B[::-1]: # reversed(B)도 가능
	print(A*int(digit))
print(A*int(B))