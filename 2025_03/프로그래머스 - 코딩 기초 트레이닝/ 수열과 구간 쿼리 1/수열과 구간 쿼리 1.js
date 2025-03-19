function solution(arr, queries) {
  for(let i = 0 ; i < queries.length ; i++){
    let [s, e] = queries[i]
    for(let j = s ; j <= e ;j++){
      arr[j]++
    }
  }

  return arr
}

// 이 풀이 좋다 ,,
function solution(arr, queries) {
  queries.forEach(([s, e]) => {
      while (s <= e) arr[s++]++;
  });
  return arr;
}