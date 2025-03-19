// 지워야하는 인덱스를 뒤에서부터 지우면 인덱스가 땡겨지는거 고려 안해도 됨
function solution(my_string, indices) {
  var answer = Array.from(my_string);
  indices.sort((a, b) => b-a).forEach(v => {
    delete answer[v]
  })
  return answer.join("");
}