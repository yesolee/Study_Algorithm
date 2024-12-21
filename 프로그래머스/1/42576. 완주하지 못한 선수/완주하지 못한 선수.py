def solution(participant, completion):
    answer = {}

    for i in participant:
        answer[i] = answer.get(i,0) + 1

    for i in completion:
        answer[i] = answer.get(i) - 1

    for key,value in answer.items():
        if value==1:
            return key