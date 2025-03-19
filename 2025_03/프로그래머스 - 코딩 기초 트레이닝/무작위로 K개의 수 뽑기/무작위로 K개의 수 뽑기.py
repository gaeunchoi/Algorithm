def solution(arr, k):
    result = []
    for ele in arr:
        if ele not in result:
            result.append(ele)
        if len(result) == k:
            break
    return result + [-1]*(k - len(result))