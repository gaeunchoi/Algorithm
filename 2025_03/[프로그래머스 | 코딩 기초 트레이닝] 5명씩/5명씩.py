def solution(names):
    answer = [names[0]]
    for i in range(5, len(names), 5):
        answer.append(names[i]);
    return answer

print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))