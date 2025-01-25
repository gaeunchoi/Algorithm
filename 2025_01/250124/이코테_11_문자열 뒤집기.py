data = list(map(int, input().rstrip()))
cnt0 = 0    # 0으로 바꾸기
cnt1 = 0    # 1로 바꾸기

if data[0] == 1:
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == 1:
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))