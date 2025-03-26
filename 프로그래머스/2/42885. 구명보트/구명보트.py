from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0

    while people:
        if len(people) >= 2 and people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.pop()
        answer += 1
    
    return answer
