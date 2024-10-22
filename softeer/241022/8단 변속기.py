DCT = list(map(int, input().split()))

num_state = -1
state = ['ascending', 'descending', 'mixed']

if DCT[0] == 1:
    for i in range(len(DCT)):
        if DCT[i] != i+1:
            num_state = 2
            break
        else:
            num_state = 0
else:
    for i in range(len(DCT)):
        if DCT[i] != 8-i:
            num_state = 2
            break
        else:
            num_state = 1

print(state[num_state])

# --------------------------------------
# 정렬 사용 
asc = sorted(DCT)
des = sorted(DCT, reversed = True)
if DCT == asc:
    print('ascending')
elif DCT == des:
    print('descending')
else:
    print('mixed')
