import sys
K, P, N = map(int, input().split())

# # 0.1초당 P배 증가
# for i in range(10*N):
#     K = (K * P) % 1000000007
#     # print(K)

def virus(a, b):
    if b == 1:
        return a
    elif b%2 == 0:
        num = virus(a, b/2)
        return (num * num) % 1000000007
    else:
        num = virus(a, (b-1)/2)
        return (num * num * a) % 1000000007

result = virus(P, 10 * N) * K
print(result % 1000000007)