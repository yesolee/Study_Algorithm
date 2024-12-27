import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return count
        elif scoville and first < K:
            count += 1
            second = heapq.heappop(scoville)
            new = first + second * 2
            heapq.heappush(scoville, new)
        else :
            return -1
