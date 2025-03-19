// 문자열 spread
const solution = (number) => [...number].reduce((a, b) => +a + +b)%9