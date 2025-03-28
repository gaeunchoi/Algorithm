// 시작 코드
// n = 입국 심사 기다리는 사람 수
// times = 심사관마다 걸리는 시간 배열
function solution(n, times) {
  let low = 1;
  let high = Math.max(...times) * n
  let answer = high;

  while(low <= high){
    let mid = Math.floor((low + high) / 2);
    let total = 0;
    
    for(let time of times){
      total += Math.floor(mid / time);
    }

    if(total >= n){
      answer = mid;
      high = mid-1;
    } else {
      low = mid + 1;
    }
  }
  return answer
}

// 테스트 실행
console.log(solution(6, [7, 10])); // 28