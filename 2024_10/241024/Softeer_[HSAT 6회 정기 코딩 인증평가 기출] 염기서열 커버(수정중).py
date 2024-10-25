import sys

N, M = map(int, input().split())
DNA = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

is_able = [True for _ in range(N)]

def check_base(A, B, result):
    base = []
    for k in range(M):
        if A[k] == B[k] or A[k] == '.':
            base.append(B[k])
        elif B[k] == '.':
            base.append(A[k])
        else:
            base.append('x')

    if base not in result:
        result.append(base)

    return result

def check_able(result):
    able = []
    for element in DNA:
        check = True
        for base in result:
            for i in range(len(element)):
                if element[i] == base[i] or element[i] == '.' or base[i] == '.':
                    check = True
                else:
                    check = False
                    break

            if check == True:
                break
            else:
                continue
        able.append(check)
    return able

def check_unable(result):
    return_result = []
    for element in result:
        if 'x' not in element:
            return_result.append(element)

    return return_result

# 처음 입력받아서 모든 조합 표시
ans = []
for i in range(1, N):
    for j in range(i):
        A, B = DNA[i], DNA[j]
        ans = check_base(A, B, ans)

# 불가능한 조합들 삭제 후 남은 조합들 중 불가능이 있는지 확인
ans = check_unable(ans)
if len(ans) == 0:
    result = N
else:
    is_able = check_able(ans)
    print(is_able)
    if is_able == True:
        result = len(ans)


print(result)

# print(ans)

# # all_cover = ans
# # for i in range(1, len(ans)):
# #     for j in range(i):
# #         A, B = ans[i], ans[j]
# #         all_cover = check_base(A, B, all_cover)
#
# all_cover = check_unable(all_cover)
# print('all cover: ', all_cover)

cnt = is_able.count(False)

# ---------------------------------------------------팡연이 코드
# import sys
# input = sys.stdin.readline
#
# input = open('input.txt', 'r').readline
#
# N, M = map(int, input().split())
# G = [input().rstrip() for _ in range(N)]
# MAX = 1<<N
#
# S = ['']*MAX
# S[0] = '.'*M
# for i in range(1, MAX):
#     k = 0
#     while not i & 1<<k:
#         k += 1
#
#     s1, s2 = G[k], S[i^(1<<k)]
#     if s1 and s2:
#         s = ''
#         for j in range(M):
#             if s1[j] == '.':
#                 s += s2[j]
#             elif s2[j] == '.':
#                 s += s1[j]
#             elif s1[j] == s2[j]:
#                 s += s1[j]
#             else:
#                 s = ''
#                 break
#         S[i] = s
#
# ans = [N]*MAX
# for i in range(1, MAX):
#     if not S[i]:
#         bits = []
#         j = 0
#         while i >= 1<<j:
#             if i&(1<<j):
#                 bits.append(j)
#             j += 1
#
#         k = 0
#         for _ in range((1<<len(bits)-1)-1):
#             for bt in bits:
#                 k ^= 1<<bt
#                 if k & (1<<bt):
#                     break
#             ans[i] = min(ans[i], ans[k]+ans[i^k])
#     else:
#         ans[i] = 1
# print(ans[-1])
