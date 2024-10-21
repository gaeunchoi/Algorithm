a, b, d = map(int, input().split())

t = 0 

goandstop, remain = divmod(d, a)
t += goandstop * a + remain if goandstop == 1 and remain == 0 else goandstop * (a + b) + remain

goandstop, remain = divmod(d, b)
t += goandstop * b + remain if goandstop == 1 and remain == 0 else goandstop * (a + b) + remain

print(t)

