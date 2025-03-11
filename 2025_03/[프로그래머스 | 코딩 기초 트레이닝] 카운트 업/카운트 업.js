// end - start + 1로 개수 체크, i 이용해서 x 기준으로 1씩 증가시키기
const solution = (s, e) => Array(e-s+1).fill(s).map((x, i) => x+i)