def solution(money, costs):
    answer = 0

    unit_list = [1,5,10,50,100,500]

    unit_costs_list = []
    for i in range(6):
        unit_costs_list.append([unit_list[i], costs[i]])

    print(unit_costs_list)

    temp = 5
    for i in range(5):
        print(unit_costs_list[i][1] * temp,' <= ', unit_costs_list[i+1][1])
        if unit_costs_list[i][1] * temp <= unit_costs_list[i+1][1]:
            print(unit_costs_list[i+1])
            del unit_costs_list[i+1]


        if temp == 5:
            temp = 2
        else:
            temp = 5


    print(unit_costs_list)



    return answer

print(solution(4578, [1, 4, 99, 35, 50, 1000]))