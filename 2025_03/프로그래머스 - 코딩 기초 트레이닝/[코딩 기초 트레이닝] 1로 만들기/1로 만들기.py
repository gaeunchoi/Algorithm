def solution(num_list):
    answer = 0

    for n in num_list:
        # 홀수일 때 1빼고 2로 나누기 -> 몫만 갖고싶다는 의미
        while n != 1:
            n //= 2
            answer += 1

    return answer
