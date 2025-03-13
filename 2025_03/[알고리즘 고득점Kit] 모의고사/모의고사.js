// 정답 개수가 찍는 패턴 개수보다 길 수도 있으니 나머지 연산으로 반복하게 해야함
// 큰 값이 여러개면 다 result에 추가해야하니 max(score)랑 비교
function solution(answers) {
  var answer = [];
  const p1 = [1, 2, 3, 4, 5];
  const p2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let score1 = answers.filter((ans, idx) => ans === p1[idx % p1.length]).length;
  let score2 = answers.filter((ans, idx) => ans === p2[idx % p2.length]).length;
  let score3 = answers.filter((ans, idx) => ans === p3[idx % p3.length]).length;
  const max = Math.max(score1, score2, score3);

  if(score1 === max) answer.push(1);
  if(score2 === max) answer.push(2);
  if(score3 === max) answer.push(3);
    
  return answer;
}