function solution(str_list, ex) {
    let result = '';

    for(let i = 0; i < str_list.length; i++) {
        if(!str_list[i].includes(ex)) {
            result += str_list[i];
        }
    }    

    return result;
}

// reduce 이용 풀이
function solution(str_list, ex) {
  return str_list.reduce((acc, cur) => {
    if(cur.includes(ex)) return acc;
    return acc+cur;
  }, "");
}