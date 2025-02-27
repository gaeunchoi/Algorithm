function solution(num_list){
    let m = 1, s = 0;
    for(let i = 0 ; i < num_list.length; i++){
        m *= num_list[i];
        s += num_list[i]
    }

    return m < s ** 2 ? 1 : 0;
}