function solution(board, k) {
  let answer = 0;
  for (let x = 0; x < board.length; x++) {
    for (let y = 0; y < board[0].length; y++) {
      if (x + y <= k) answer += board[x][y];
    }
  }
  return answer;
}