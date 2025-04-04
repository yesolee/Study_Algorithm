##### 아이디어
# 지수가 가장 낮은 두개 => 새로운 원소 다시 넣음 : 최소힙
# 모든 값이 k 이상이 될 때까지 반복 => 루트 노드가 k 이상일때까지 반복
# 루트노드가 k가 될때까지 섞는 최소 횟수를 return
### 실패조건: 값을 만족하는게 없으면 -1
### 케이스1: 음식이 이미 다 k 이상이면? 0번 섞고 끝내기
### 케이스2: 1개만 남았는데 k 이상이 안되면?
### 케이스3: 2개인데 섞어도 k 이상이 안되면?

##### 시간복잡도
# scoville 길이 1백만 => n^2는 절대 안 됨!
#  100만일때, n log n은 약 2천만이라 가능
# 최대 n-1번 섞고, 각 섞기마다 log n 소요 => n log n
# 왜냐하면 힙에서 pop/push는 각 각 log n
# 작은거 2개 뽑고 섞은거 넣어야하니까 => 총 3번의 log n (그냥 log n)

##### 자료구조
# result :  int
# 조건 만족 못하면 -1

import heapq

def solution(scoville, k):

    # 최소힙
    heapq.heapify(scoville)
    
    # 카운팅
    cnt = 0
    while len(scoville)>1 :
        if scoville[0] >= k:
            return cnt
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        cnt += 1
    
    if scoville[0] >= k:
        return cnt
    # 조건만족 못하면 -1 반환
    return -1