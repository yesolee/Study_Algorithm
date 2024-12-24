def solution(priorities, location):
    order = [[i,v]for i,v in enumerate(priorities)]
    excution = []

    while len(order):
        temp = order.pop(0)
        if len(order) and temp[1] < max([i[1] for i in order]):
            order.append(temp)
        else:
            excution.append(temp[0])

    return excution.index(location) + 1