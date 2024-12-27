1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer

# 메모리: 51.8 MB, 시간: 1585.97 ms

# import heapq

# def solution(scoville, K):
#     heapq.heapify(scoville)
#     count = 0
#     while scoville:
#         first = heapq.heappop(scoville)
#         if first >= K:
#             return count
#         if not scoville:
#             return -1
#         count += 1
#         second = heapq.heappop(scoville)
#         new = first + second * 2
#         heapq.heappush(scoville, new)

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