# 0번 인덱스부터 2칸씩 / 1번 인덱스부터 2칸씩 찢으면 홀짝 인덱스 합 구하기 가능
def solution(num_list):
  return max(sum(num_list[::2]), sum(num_list[1::2]))