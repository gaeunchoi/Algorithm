// 모드 전환 비트 뒤집기, 조건이 겹치는게 있으니 큰 조건먼저 체크
function solution(code) {
  var answer = '';
  let mode = 0
  for(let i = 0 ; i < code.length ; i++){
    if(code[i] === '1') mode ^= 1
    else{
      if(i % 2 == mode) answer += code[i]
    }
  }
  return answer.length > 0 ? answer : "EMPTY";
}