from math import sqrt
N = int(input())

print(int(sqrt(N)))
#    1 2 3 4 5 6 7 8 9 10
# 1  o o o o o o o o o o
# 2  o x o x o x o x o x
# 3  o x x x o o o x x x
# 4  o x x o o o o o x x
# 5  o x x o x o o o x o
# 6  o x x o x x o o x o
# 7  o x x o x x x o x o
# 8  o x x o x x x x x o
# 9  o x x o x x x x o o
# 10 o x x o x x x x o x

# N = 1 -> 1
# N = 2 -> 1
# N = 3 -> 1
# N = 4 -> 2
# N = 5 -> 2
# N = 6 -> 2
# N = 7 -> 2
# N = 8 -> 2
# N = 9 -> 3
# N = 10 -> 3