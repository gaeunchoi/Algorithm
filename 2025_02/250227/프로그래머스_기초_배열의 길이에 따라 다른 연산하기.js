function solution(arr, n){
    let l = arr.length;

    return (l % 2 === 1) 
    ? arr.map((v, i) => i % 2 === 0 ? v + n : v)
    : arr.map((v, i) => i % 2 === 1 ? v + n : v);
}