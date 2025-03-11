def solution(numbers):
    answer = ''
    num = list(map(str, numbers))
    #천의 자리로 맞춰주기
    
    # s = sorted(num, reverse=True)
    s = sorted(num,key=lambda x: x*3,reverse=True)
    answer += ''.join(s)
    return str(int(answer))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))