import sys

T = int(input())

for _ in range(T):
    cnt = int(sys.stdin.readline())
    sym_plus, sym_bar = divmod(cnt, 5)
    print('++++ ' * sym_plus,  end = ' ')
    print('|' * sym_bar)