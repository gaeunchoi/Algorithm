function solution(arr, divisor) {
  let result = []
  arr.forEach(v => {
    if(v % divisor === 0) result.push(v)
  })
  return result.length ? result.sort((a, b) => a-b) : [-1]
}

// 좋아요 많이 받은 풀이
function solution(arr, divisor) {
  var answer = arr.filter(v => v%divisor == 0);
  return answer.length == 0 ? [-1] : answer.sort((a,b) => a-b);
}