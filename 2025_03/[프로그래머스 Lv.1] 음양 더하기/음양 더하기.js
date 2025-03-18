function solution(absolutes, signs) {
  let result = 0
  for(let i = 0 ; i < absolutes.length ;i++){
    result += signs[i] ? absolutes[i] : -absolutes[i]
  }
  return result
}

// reduce 이용 풀이
function solution(absolutes, signs) {
  return absolutes.reduce((acc, val, i) => acc + (val * (signs[i] ? 1 : -1)), 0);
}