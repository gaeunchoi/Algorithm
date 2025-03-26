// 내림차순 정렬 -> 큰거부터 묶기
function solution(k, m, score) {
  score.sort((a, b) => b - a);
  let answer = 0;
  for(let i = 0 ; i < score.length ; i += m){
    const box = score.slice(i, i + m);
    const min = box[m-1];
    if(min) answer += m * min;
  }
  return answer;
}