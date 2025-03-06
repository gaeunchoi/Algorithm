def solution(n, lost, reserve):
    # reserve <-> lost 간의 중복이 있을 수 있다
    # set으로 변환해주고, 
    lost, reserve = set(lost), set(reserve)
    reserve_s, lost_s = set(reserve) - set(lost), set(lost) - set(reserve)

    for extra in sorted(reserve_s):
        if extra-1 in lost_s:
           lost_s.remove(extra-1)
        elif extra+1 in lost_s:
           lost_s.remove(extra+1)

    return n - len(lost_s)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))