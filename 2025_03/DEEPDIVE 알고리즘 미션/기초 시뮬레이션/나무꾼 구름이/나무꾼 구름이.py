N, M, xs = map(int, input().split(" "))
H = list(map(int, input().split(" ")))
Q = int(input())
D = list(map(str, input().split(" ")))

result = 0
pos = xs - 1
for idx in range(Q):
  if H[pos] + idx >= M:
    result += H[pos] + idx
    H[pos] -= H[pos] + idx

  if D[idx] == 'L':
    pos = (pos-1+N) % N
  elif D[idx] == 'R':
    pos = (pos+1) % N
print(result)