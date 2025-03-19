// idx기준 1->0, 2->1을 봐야하니 numLog 1부터 슬라이스치고 map 걸면 i로 이전인덱스 접근 가능
function solution(numLog) {
  var answer = '';
  
  const order = {
    '1': 'w',
    '-1': 's',
    '10': 'd',
    '-10': 'a'
  };

  return numLog.slice(1).map((v, i) => order[v - numLog[i]]).join('')
}