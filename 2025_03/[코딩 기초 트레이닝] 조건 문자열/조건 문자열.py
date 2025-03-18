def solution(ineq, eq, n, m):
    answer = 0
    if n > m and ineq ==">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer

  
# 아이디어 쩐디 ,, 근데 eval은 쓰면안됨 ㅇㅅㅇ
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))