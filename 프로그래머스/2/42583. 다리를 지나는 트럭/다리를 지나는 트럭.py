def solution(bridge_length, weight, truck_weights):
    time = 0
    temp_w = 0
    bridge = []
    while truck_weights:
        time += 1
        if len(bridge) == bridge_length :
            truck = bridge.pop(0)
            temp_w -= truck

        if temp_w + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            temp_w += truck

        else:
            bridge.append(0)

    return time+bridge_length if bridge_length > 1 else time