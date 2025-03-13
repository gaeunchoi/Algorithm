from collections import deque
def solution(bridge_length, weight, truck_weights):
    t = 0                                   # 소요시간
    bridge = deque([0] * bridge_length)     # 다리 위
    current_weight = 0                      # 다리 위 트럭 무게

    while truck_weights:
        t += 1
        current_weight -= bridge.popleft()  # 맨 앞에 있는 트럭이 다리를 지나면 무게 줄어듬

        # 다리 위 트럭 무게 + 새로운 트럭 <= 다리가 견딜 수 있는 무게라면
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]      # 대기하고 있던 트럭 무게를 다리위 트럭 무게에 더해주기
            bridge.append(truck_weights.pop(0))     # 대기하고 있던 트럭 출발~
        else:
            bridge.append(0)                        # 다리에 0을 추가해 자리 이동 표시

    t = t + bridge_length
    return t

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))