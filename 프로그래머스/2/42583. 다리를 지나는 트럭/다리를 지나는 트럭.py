def solution(bridge_length, weight, truck_weights):
    time = 0
    temp_w = 0
    bridge = [0] * bridge_length
    while truck_weights or temp_w:
        time += 1
        truck =bridge.pop(0)
        temp_w -= truck

        if truck_weights and (temp_w + truck_weights[0] <= weight):
            truck = truck_weights.pop(0)
            bridge.append(truck)
            temp_w += truck

        else:
            bridge.append(0)

    return time
