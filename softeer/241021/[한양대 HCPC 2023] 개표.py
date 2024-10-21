import sys

T = int(input())

for _ in range(T):
    cnt = int(sys.stdin.readline())
    sym_plus, sym_bar = divmod(cnt, 5)

    for i in range(sym_plus):
        print('++++', end = ' ')
    
    for i in range(sym_bar):
        print('|', end = '')

    print('')
