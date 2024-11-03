def solution(name, yearning, photo):
    answer = [0] * len(photo)
    scores = {}
    for i in range(len(name)):
        scores[name[i]] = yearning[i]
    
    for i in range(len(photo)):
        for j in photo[i]:
            answer[i] += scores[j] if j in scores.keys() else 0
        
    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"],[11, 1, 55],[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may"],["kein", "deny", "may"], ["kon", "coni"]]))