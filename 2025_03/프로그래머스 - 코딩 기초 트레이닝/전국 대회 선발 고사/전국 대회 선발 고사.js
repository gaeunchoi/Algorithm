// 참여 안하는사람 거르고 점수순으로 정렬 -> filter를 써도 될것같은디 
function solution(rank, attendance) {
  var answer = [];
  rank.forEach((score, i) => {
    if(attendance[i]) answer.push([score, i]) 
  })

  answer.sort((a, b) => {
    if(a[0] > b[0]) return 1;
    if(a[0] < b[0]) return -1
  })

  return 10000*answer[0][1] + 100*answer[1][1] + answer[2][1];
}


// 천잰가 이분은 .. ?
function solution(rank, attendance) {
  const [a, b, c] = rank
    .map((r, i) => [r, i])
    .filter(([_, i]) => attendance[i])
    .sort(([a], [b]) => a - b);
  return 10000 * a[1] + 100 * b[1] + c[1];
}