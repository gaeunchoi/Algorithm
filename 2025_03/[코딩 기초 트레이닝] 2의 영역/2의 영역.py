# 뒤집고 뒤에서부터 나오는 2 인덱스 찾으면 됨
def solution(arr):
  if 2 not in arr:
    return [-1]
  return arr[arr.index(2): len(arr) - arr[::-1].index(2)]