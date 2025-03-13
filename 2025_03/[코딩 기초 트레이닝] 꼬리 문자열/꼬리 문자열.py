def solution(str_list, ex):
    answer = ''
    for str in str_list:
        if ex not in str:
            answer += str_list
    return 

# lambda 이용 풀이
def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))