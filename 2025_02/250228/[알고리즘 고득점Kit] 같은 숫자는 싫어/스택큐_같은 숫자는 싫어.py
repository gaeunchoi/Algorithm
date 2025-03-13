def solution(arr):
    answer = [arr[0]]
    for ele in arr:
        if answer[-1] != ele:
            answer.append(ele)
        else:
            continue
    return answer

# if answer[-1:] == [i] continue 로 하면 빈배열에 써도 안죽는다 ..

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))