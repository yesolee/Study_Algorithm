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

# 메모리: 51.8 MB, 시간: 1613.05 ms
# import heapq

# def solution(scoville, K):
#     heapq.heapify(scoville)
#     count = 0
#     while scoville:
#         first = heapq.heappop(scoville)
#         if first >= K:
#             return count
#         elif scoville and first < K:
#             count += 1
#             second = heapq.heappop(scoville)
#             new = first + second * 2
#             heapq.heappush(scoville, new)
#         else :
#             return -1