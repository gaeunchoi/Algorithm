# T = int(input())
#
# nums = {0 : [1,2,3,4,5,6], 1: [5, 6], 2: [1,3,4,6,7], 3: [1,4,5,6,7], 4: [2,5,6,7], 5: [1,2,4,5,7], 6:[1,2,3,4,5,7], 7: [1,2,5,6], 8: [1,2,3,4,5,6,7], 9: [1,2,4,5,6,7]}
#
# for _ in range(T):
#     result = 0
#     a, b = map(int, input().split())
#
#     # 10000의 자리
#     A = [0] * 5
#     B = [0] * 5
#     A[0], B[0] = a // 10000, b // 10000
#     A[1], B[1] = (a % 10000) // 1000, (b % 10000) // 1000
#     A[2], B[2] = (a % 1000) // 100, (b % 1000) // 100
#     A[3], B[3] = (a % 100) // 10, (b % 100) // 10
#     A[4], B[4] = a % 10, b % 10
#
#     for i in range(5):
#         onoff = set()
#         if (i == 0 and A[i] == 0 and B[i] == 0) or (i != 0 and A[i-1] == 0 and B[i-1] == 0  and A[i] == 0 and B[i] == 0):
#             tmp = set()
#         elif (i == 0 and A[i] == 0) or (i != 0 and A[i-1] == 0 and A[i] == 0):
#             tmp = set(nums[B[i]])
#         elif (i == 0 and B[i] == 0) or (i != 0 and B[i-1] == 0 and B[i] == 0):
#             tmp = set(nums[A[i]])
#         else:
#             onoff = set(nums[A[i]]) & set(nums[B[i]])
#             tmp = set(nums[A[i]]) | (set(nums[B[i]]))
#
#         result += len(tmp.difference(onoff))
#
#     print(result)

# 풀이코드
import sys
light = {
    "0" : "1110111",
    "1" : "0010010",
    "2" : "1011101",
    "3" : "1011011",
    "4" : "0111010",
    "5" : "1101011",
    "6" : "1101111",
    "7" : "1110010",
    "8" : "1111111",
    "9" : "1111011",
    " " : "0000000"
}

t = int(input())
for k in range(t):
    a, b = input().split()
    a = (5 - len(a))*" " + a
    b = (5 - len(b))*" " + b

    total = 0
    for i in range(5):
        for j in range(7):
            total += (light[a[i]][j] != light[b[i]][j]) # True면 1, False면 0
    print(total)