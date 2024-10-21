import sys
M, N, K = map(int, input().split())

keys = list(map(int, input().split()))
buttons = list(map(int, input().split()))

menu = 0
for i in range(N-2):
    tmp = buttons[i:i+M]
    if keys == tmp:
        menu = 1

if menu == 1:
    print("secret")
else:
    print("normal")
