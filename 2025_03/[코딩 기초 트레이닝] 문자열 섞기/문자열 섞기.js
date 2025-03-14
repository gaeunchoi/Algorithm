function solution(str1, str2) {
  var answer = '';
  for(let i = 0 ; i< str1.length ; i++){
    answer += str1[i] + str2[i]
  }
  return answer;
}

// 와 이건 상상도 못했ㄴㅔ..
function solution(str1, str2) {
  return [...str1].map((x, idx)=> x+str2[idx]).join("");
}