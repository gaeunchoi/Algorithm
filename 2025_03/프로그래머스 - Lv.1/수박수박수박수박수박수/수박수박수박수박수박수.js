function solution(n) {
  var answer = '';
  for(let i = 0 ; i < n ; i++){
    answer += i % 2 === 0 ? '수' : '박'
  }
  return answer;
}


// 풀이 좋다 ,,
const waterMelon = n => "수박".repeat(n).slice(0,n);