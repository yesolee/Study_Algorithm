def solution(n, lost, reserve):

    lost.sort()
    reserve.sort()
    
    answer = 0
    # 여벌 체육복이 있는 학생이 도난당한 경우 빌려줄 수 없음(=반드시 자기꺼 입어야함)
    # 반례: 5, [2, 3], [3, 4]
    # 여벌 체육복이 있는 학생 중 도난당한 학생부터 먼저 처리해야함
    
    real_lost = []
    
    for student in lost:
        if student not in reserve:
            real_lost.append(student)
        if reserve and student in reserve:
            reserve.remove(student)
            
    for student in real_lost:
        # 작은 값을 먼저 확인하므로 정렬이 필요함
        # 반례: 5, [4, 2], [3, 5]
        if reserve and student-1 in reserve:
            reserve.remove(student-1)
            answer += 1
            continue
    
        if reserve and student+1 in reserve:
            reserve.remove(student+1)
            answer += 1
            
    return n-len(real_lost)+answer
