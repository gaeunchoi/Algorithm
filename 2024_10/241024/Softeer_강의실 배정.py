import sys

N = int(input())
lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lectures = sorted(lectures, key = lambda x: x[1])

result = 0
end = 0
for lecture in lectures:
    st, et = lecture
    if st >= end:
        end = et
        result += 1

print(result)