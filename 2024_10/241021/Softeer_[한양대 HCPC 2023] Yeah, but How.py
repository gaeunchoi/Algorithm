import sys

input_str = sys.stdin.readline().rstrip()
print(input_str.replace('()', '(1)').replace(')(', ')+('))

# ------------------------------------------------------------------------------------
# from collections import deque
# import sys
#
# input_str = deque(sys.stdin.readline())
# result = deque()
#
# isFirst = True
#
# left_sym = input_str.popleft()
# current_sym = input_str.popleft()
#
# while left_sym != '\n':
#     result.append(left_sym)
#
#     if isFirst == True:
#         isFirst = False
#     else:
#         current_sym = input_str.popleft()
#
#     if left_sym == '(' and current_sym == '(':
#         result.append('1+')
#     if left_sym == '(' and current_sym == ')':
#         result.append('1')
#     if left_sym == ')' and current_sym == '(':
#         result.append('+')
#     if left_sym == ')' and current_sym == ')':
#         result.append('+1')
#
#     left_sym = current_sym
#
# for i in range(len(result)):
#     print(result[i], end='')