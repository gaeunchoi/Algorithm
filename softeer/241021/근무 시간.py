import sys

result = 0
for i in range(5):
    st_h, et_h = sys.stdin.readline().rstrip().split()
    st_h, et_h = st_h.split(':'), et_h.split(':')
    st = int(st_h[0]) * 60 + int(st_h[1])
    et = int(et_h[0]) * 60 + int(et_h[1])
    result += et - st

print(result)