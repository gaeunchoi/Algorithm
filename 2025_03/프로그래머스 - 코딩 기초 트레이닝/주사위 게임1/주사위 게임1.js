function solution(a, b) {
  const Aodd = a%2 === 1
  const Bodd = b%2 === 1

  if(Aodd && Bodd) return a**2 + b**2
  if(!Aodd && !Bodd) return Math.abs(a-b)
  return 2*(a+b)
}