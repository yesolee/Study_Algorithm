def solution(people, limit):
    # 최대 2명만 탈 수 있음 => 제일 무거운 애 + 제일 가벼운 애
    people.sort()
    left=0
    right = len(people) - 1
    answer = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        # 굳이 pop 할 필요없이 다음턴으로 넘어가면 됨   
        right -= 1
        answer += 1

    return answer

# from collections import deque

# def solution(people, limit):
#     people.sort()
#     people = deque(people)
#     answer = 0

#     while people:
#         if len(people) >= 2 and people[0] + people[-1] <= limit:
#             people.popleft()
#             people.pop()
#         else:
#             people.pop()
#         answer += 1
    
#     return answer