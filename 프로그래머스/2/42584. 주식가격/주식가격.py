from collections import deque

def solution(prices):
    prices = deque(prices)
    answer= []
    while prices:
        item = prices.popleft()
        count = 0
        if not prices:
            answer.append(0)
            break

        for i in prices :
            count += 1
            if item > i:
                break
        answer.append(count)
    return answer