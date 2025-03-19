function solution(price, money, count){
  let m = 0;
  for(let i = 1 ; i <= count ; i++){
    m += price*i
  }

  return money > m  ? 0 : m - money
}

// 가우스 공식 사용
function solution(price, money, count) {
  const tmp = price * count * (count + 1) / 2 - money;
  return tmp > 0 ? tmp : 0;
}