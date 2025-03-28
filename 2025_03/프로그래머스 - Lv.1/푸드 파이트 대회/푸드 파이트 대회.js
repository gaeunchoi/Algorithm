function solution(food) {
  let answer = food.map((val, idx) => {
    return String(idx).repeat(Math.floor(food[idx]/2));
  });
  return answer.join("") + "0" + answer.reverse().join("");
}