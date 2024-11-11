def solution(today, terms, privacies):
    answer = []
    ty, tm, td = map(int, today.split('.'))
    expiration = {}

    for term in terms:
        t, m = term.split()
        expiration[t] = int(m) * 28

    for i in range(len(privacies)):
        date, type = privacies[i].split()
        dy, dm, dd = map(int, date.split('.'))
        y, m, d = ty - dy, tm - dm, td - dd

        total = y * 336 + m * 28 + d
        if expiration[type] <= total:
            answer.append(i+1)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))