##### 아이디어
# 우선순위큐 정렬순서: 최소힙 - 소요시간, 요청시점, 작업번호
# 한번 작업하면 마칠때까지 수행
# 종료하자마자 들어오면 대기 들어갔다 나옴
# 작업과 작업 사이는 소요 시간 필요X 0초 =>요청시간==현재시간
# 작업 요청이 순서대로 들어온다는 조건이 없음 => 정렬 필요
## 종료조건: 큐도 비고, 남은 작업도 없을 때까지
## 예외상황: 작업중인게 없는데 요청이 없는 경우 => 시간 +1하면서 기다려야함


##### 시간복잡도
# n = 500번 => n^2도 가능!
# 처음 작업 순서 정렬 필요 : sort => nlogn
# heappush는 최대 n번 => nlogn
# heappop은 최대 n번 => nlogn

##### 자료구조
# 대기큐: 작업번호, 요청시각, 소요시간
# 반환: 반환시간의 평균 정수부분(몫) => 반환시간합계//작업수


import heapq

def solution(jobs):
    # 요청 시점 순서대로 정렬
    jobs.sort() # 시간복잡도 nlogn
    
    # 우선순위 대기큐 생성
    waiting = []
    
    # jobs 요소 확인할 인덱스
    idx = 0
    curTime = 0
    returnTime = 0 # 반환시간 = 종료시점 - 요청시점
    n = len(jobs) 
    
    # 종료시점: 작업을 마치고, 대기큐에도 작업이 없는 경우
    while idx < n or waiting:
        
        # 현재 시점까지 요청된 작업을 대기큐에 넣기
        while idx<n and jobs[idx][0] <= curTime:
            start, duration = jobs[idx]
            # 대기 큐 우선순위 - 소요시간, 요청시점, 작업번호
            heapq.heappush(waiting, (duration, start, idx))
            idx += 1
        
        # 대기큐에 처리할 작업이 있는 경우 실행
        if waiting:
            duration, start, job_id = heapq.heappop(waiting)
            curTime += duration
            returnTime += curTime - start
        else:
            # 처리할 작업이 없는 경우, 다음 작업시간으로 점프
            curTime = jobs[idx][0]
    
    return returnTime // n


