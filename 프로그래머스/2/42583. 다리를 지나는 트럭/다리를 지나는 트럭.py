# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     temp_w = 0
#     bridge = []
#     while truck_weights:
#         time += 1
#         if len(bridge) == bridge_length :
#             truck = bridge.pop(0)
#             temp_w -= truck

#         if temp_w + truck_weights[0] <= weight:
#             truck = truck_weights.pop(0)
#             bridge.append(truck)
#             temp_w += truck

#         else:
#             bridge.append(0)

#     return time+bridge_length if bridge_length > 1 else time

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 길이만큼 초기화
    temp_w = 0  # 현재 다리 위 트럭 무게 합계

    while truck_weights or temp_w > 0:  # 대기 트럭이 있거나 다리 위에 트럭이 있는 동안 반복
        time += 1
        # 다리에서 트럭(또는 빈 공간) 제거
        temp_w -= bridge.popleft()

        if truck_weights and temp_w + truck_weights[0] <= weight:
            # 새로운 트럭 추가
            truck = truck_weights.pop(0)
            bridge.append(truck)
            temp_w += truck
        else:
            # 트럭이 못 올라오면 빈 공간 추가
            bridge.append(0)

    return time
