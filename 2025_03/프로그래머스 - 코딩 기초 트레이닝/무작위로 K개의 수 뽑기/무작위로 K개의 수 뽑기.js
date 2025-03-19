function solution(arr, k) {
  var answer = [];
  for(let i = 0 ; i < arr.length ; i++){
    if(!answer.includes(arr[i])) answer.push(arr[i])
    if(answer.length === k) break
  }
  return answer.concat(Array(k - answer.length).fill(-1));
}


// js는 Set해도 자동 정렬이 안된다 oh ..
function solution(arr, k) {
  const set = new Set(arr);
  return set.size < k ? [...set, ...Array(k - set.size).fill(-1)] : [...set].slice(0, k);
}