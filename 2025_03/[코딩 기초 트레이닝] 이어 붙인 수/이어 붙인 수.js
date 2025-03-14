function solution(num_list) {
  let oddSum = '', evenSum = '';
  num_list.forEach((num) => {
    if(num%2 === 0){
    evenSum += num
    } else {
      oddSum += num
    }
  })
  
  return +oddSum + +evenSum;
}