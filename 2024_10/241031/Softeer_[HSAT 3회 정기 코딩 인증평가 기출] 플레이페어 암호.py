import sys

message = input()
keys = list(set(input()))
key_maps = [[''] * 5 for _ in range(5)]

# 입력받은거에서 중복 제거하고, 그 뒤에 알파벳 붙이기
for i in range(ord('A'), ord('Z') + 1):
    char = chr(i)

    if char not in keys and char != 'J':
        keys.append(char)

# 맵 셋팅
for i in range(25):
    key_maps[i // 5][i % 5] = keys[i]
# print(key_maps)

# LL -> LX LX
# XX -> XQ XX로 분리
# HELLOWORLD -> HE LX LO WO RL DX
# XXYYY -> XQ XY YX YX
# LEMONSTRAWBERRYAPPLEIUICE -> LE MO NS TR AW BE RX RY AP PL EI UI CE
pairs = []
i = 0
while i < len(message):
    if i == len(message) - 1:
        pairs.append([message[i], 'X'])
        break

    if message[i] == message[i + 1]:
        if message[i] == 'X':
            pairs.append([message[i], 'Q'])
        else:
            pairs.append([message[i], 'X'])
        i += 1
    else:
        pairs.append([message[i], message[i + 1]])
        i += 2


def find_pos(target):
    for i in range(5):
        for j in range(5):
            if key_maps[i][j] == target:
                return i, j

# print(pairs)

result = []
for val in pairs:
    x1, y1 = find_pos(val[0])
    x2, y2 = find_pos(val[1])
    if x1 == x2:
        result.extend([key_maps[x1][(y1 + 1) % 5], key_maps[x2][(y2 + 1) % 5]])
    elif y1 == y2:
        result.extend([key_maps[(x1 + 1) % 5][y1], key_maps[(x2 + 1) % 5][y2]])
    else:
        result.extend([key_maps[x1][y2], key_maps[x2][y1]])

for val in result:
    print(val, end='')