function solution(num_list) {
  let answer = 0;
  num_list.forEach((value) => {
    while(value !== 1){
      // 홀수일때 1 빼고 2로 나누기 -> 그냥 홀수 2로 나누고 몫 구하기랑 같음
      value = Math.floor(value / 2)
      answer++;
    }
  })
  return answer;
}