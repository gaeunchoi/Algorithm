const solution = (arr) => arr.reduce((acc, cur) => [...acc, ...new Array(cur).fill(cur)], []);


console.log(solution([5, 1, 4]));
console.log(solution([6, 6]));
console.log(solution([1]));

