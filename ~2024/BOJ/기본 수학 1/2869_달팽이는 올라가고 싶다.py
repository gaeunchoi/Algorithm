import math

a, b, v = map(int, input().split())

# v-b 하는 이유? 정상에 올라가면 내려오지 않으므로 
day = (v-b) / (a-b)

print(math.ceil(day))