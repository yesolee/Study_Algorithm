# n: 10만 => n**2은 안됨
# heapq.heappush() : logn
# healq.heappop(): logn
# nlogn => 200만 미만

import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())
nums = [int(input().strip())for i in range(n)]
result = []
for num in nums:
    if num >0:
        heapq.heappush(result, num)
    elif result:
         print(heapq.heappop(result))
    else:
        print(0)