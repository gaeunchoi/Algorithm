# 내림차순으로 정렬하고, 인용수가 논문수랑 같아지는 지점 체크(논문수 1부터 증가, idx 이용)
def solution(citations):
  answer = 0
  citations.sort(reverse=True)
  for cnt, citation in enumerate(citations):
    if citation >= cnt+1:
      answer = cnt+1
  return answer


# 좋아요 많이 받은 풀이 -> 확실히 간결한데 이해도가 떨어짐
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer