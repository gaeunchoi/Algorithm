def prime_list():       # 에라토스테네스의 체로 소수 리스트 구하기
    n = 10001           # 문제에서 제시한 조건
    sieve = [True] * n

    for i in range(2, int(n ** 0.5)+1):
        if sieve[i]:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


T = int(input())

Prime = prime_list()

for i in range(T):
    n = int(input())

    a = n // 2
    b = n // 2

    while True:
        if a and b in Prime:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
