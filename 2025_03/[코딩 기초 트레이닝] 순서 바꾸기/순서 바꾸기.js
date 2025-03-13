// spread 연산자로 요소 합치기
const solution = (arr, n) => [...arr.splice(n), ...arr.splice(0, n)]