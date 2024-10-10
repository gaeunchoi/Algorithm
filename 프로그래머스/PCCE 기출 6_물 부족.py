def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage += usage * change[i]/100
        total_usage += usage
        print(usage, total_usage)
        if total_usage > storage:
            return i

    return -1

print(solution(5141, 500, [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]))
print(solution(1000, 2000, [-10, 25, -33]))