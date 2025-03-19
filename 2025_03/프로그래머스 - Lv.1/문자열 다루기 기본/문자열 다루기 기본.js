const solution = s => (s.length === 4 || s.length ===6) && s.split("").every(c => !isNaN(c)) ? true : false


// 저렇게 안해도 되네 ,, ?
// const solution = s => s.length == 4 || s.length == 6 ? !isNaN(s) : false 