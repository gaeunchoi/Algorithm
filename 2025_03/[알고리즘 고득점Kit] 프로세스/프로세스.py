from collections import deque
def solution(priorities, location):
    queue = deque((idx, pro) for idx, pro in enumerate(priorities))
    cnt = 0

    while True:
        current = queue.popleft()
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            cnt += 1
            if current[0] == location:
                return cnt

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))