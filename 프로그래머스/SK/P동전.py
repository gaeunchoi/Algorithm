def solution(money, costs):
    values = [1, 5, 10, 50, 100, 500]

    lists = []
    for i in range(len(costs)):
        lists.append([values[i], costs[i], values[i] / costs[i]])

    lists.sort(key=lambda x: x[2], reverse=True)

    print(lists)

    cnt = 0
    for coin in lists:
        tmp = money // coin[0]

        cnt += coin[1] * tmp
        money -= coin[0] * tmp

        if money == 0:
            break

    return cnt

money = int(input())

costs = list(map(int, input().split()))

answer = solution(money, costs)
print(answer)
