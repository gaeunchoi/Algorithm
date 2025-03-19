# 가로, 세로 길이를 나눠서 보지말고 긴쪽 짧은쪽으로만 정리
def solution(sizes):
  w, h = 0, 0
  for v1, v2 in sizes:
    short, long = min(v1, v2), max(v1, v2)
    w, h = max(w, short), max(h, long)

  return w*h