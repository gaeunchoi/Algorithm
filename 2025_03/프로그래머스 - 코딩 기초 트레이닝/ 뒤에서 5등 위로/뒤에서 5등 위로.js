// 오름차순 정렬 후 5개 앞에서 자르고 쭉 가져오기
const solution = num_list => num_list.sort((a, b) => a - b).slice(5)