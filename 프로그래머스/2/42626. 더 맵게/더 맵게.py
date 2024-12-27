import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return count
        if not scoville:
            return -1
        count += 1
        second = heapq.heappop(scoville)
        new = first + second * 2
        heapq.heappush(scoville, new)
