// 2차원 배열 정석대로 풀기
function solution(arr) {
  for(let i = 0 ; i < arr.length ; i++){
    for(let j = 0 ; j<arr.length ;j++){
      if(arr[i][j] !== arr[j][i]) return 0
    }
  }
  return 1
}

// 오메 every 써도 되는구나
function solution(arr) {
    return arr.every((r, i) => r.every((_, j) => arr[i][j] === arr[j][i])) ? 1 : 0;
}