function solution(citations) {
  var answer = 0;

  // 내림차순 정렬
  citations.sort((a, b) => b-a);

  // 인용 수와 논문 개수가 같아지는 지점을 체크
  [...citations].forEach((v, i) => {
    if(v >= i+1) answer = i+1
  });
  
  return answer;
}