function solution(n) {
    result = 0
    if(n%2==1){
        for(var i = 1 ; i <= n ; i+= 2){
            result += i
        }
    } else {
        for(var i = 2 ; i <= n ; i += 2){
            result += i**2
        }
    }
    return result
}