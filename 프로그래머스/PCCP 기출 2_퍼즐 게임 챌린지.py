def solve_puzzle(level, diffs, times):
    solve_time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            solve_time += times[i]
        else:
            solve_time += (diffs[i] - level) * (times[i] + times[i-1]) + times[i]

    return solve_time

def solution(diffs, times, limit):
    level_arr = [i for i in range(min(diffs), max(diffs)+1)]

    start, end = 0, len(level_arr)-1

    levelable = []
    while start <= end:
        pivot = (start + end) // 2

        if solve_puzzle(level_arr[pivot], diffs, times) <= limit:
            levelable.append(level_arr[pivot])
            end = pivot - 1
        else:
            start = pivot + 1

    answer = min(levelable)

    return answer


print(solution([1, 5, 3],[2, 4, 7],30))
print(solution([1, 4, 4, 2],[6, 3, 8, 2],59))
print(solution([1, 328, 467, 209, 54],[2, 7, 1, 4, 3],1723))
print(solution([1, 99999, 100000, 99995],[9999, 9001, 9999, 9001],3456789012))