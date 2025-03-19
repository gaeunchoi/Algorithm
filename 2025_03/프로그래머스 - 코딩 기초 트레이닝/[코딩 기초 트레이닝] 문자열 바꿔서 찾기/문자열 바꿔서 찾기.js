// 문자열 바꿔서 찾기
// "A" -> "B", "B" -> "A"
function solution(myString, pat) {
  const newStr = [...myString].reduce((acc, cur) => {
    if (cur === 'A'){
      acc += 'B';
    } else {
      acc += 'A';
    }
    return acc;
  }, '');

  return newStr.includes(pat) ? 1 : 0;
}