# from collections import deque

# def solution(prices):
#     prices = deque(prices)
#     answer= []
#     while prices:
#         item = prices.popleft()
#         count = 0
#         if not prices:
#             answer.append(0)
#             break

#         for i in prices :
#             count += 1
#             if item > i:
#                 break
#         answer.append(count)
#     return answer

def solution(prices):
    answer = [0] * len(prices)  # 결과를 저장할 리스트 초기화
    stack = []  # 스택 초기화

    for i in range(len(prices)):
        # 현재 가격이 스택에 저장된 가격보다 작으면
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()  # 스택에서 인덱스를 꺼냄
            answer[idx] = i - idx  # 현재 인덱스와 스택 인덱스의 차이를 저장
        stack.append(i)  # 현재 인덱스를 스택에 추가

    # 스택에 남아 있는 인덱스 처리
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - 1 - idx

    return answer