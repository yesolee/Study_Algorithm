# list의 in, remove => set으로 변경해 O(1)로 변경

def solution(n, lost, reserve):
    # 중복 없으므로 set으로 변환
    lost_set = set(lost)
    reserve_set =set(reserve)
    
    # 도난+여벌(자기꺼만 쓸 수 있음)
    intersection = lost_set & reserve_set
    lost_set -= intersection
    reserve_set -= intersection
    
    # 체육복 빌리기
    answer = 0
    for student in sorted(lost_set):
        if student-1 in reserve_set:
            reserve_set.remove(student-1)
            answer += 1
        elif student+1 in reserve_set:
            reserve_set.remove(student+1)
            answer += 1
        else:
            continue # 못빌림
            
    return n-len(lost_set)+answer





# 처음 풀이
# def solution(n, lost, reserve):

#     lost.sort() # L = len(lost), O(L log L)
#     reserve.sort() # R = len(reserve), O(R log R) 
    
#     answer = 0
#     # 여벌 체육복이 있는 학생이 도난당한 경우 빌려줄 수 없음(=반드시 자기꺼 입어야함)
#     # 반례: 5, [2, 3], [3, 4]
#     # 여벌 체육복이 있는 학생 중 도난당한 학생부터 먼저 처리해야함
    
#     real_lost = [] # 공간-O(L)
    
#     # O(R) 연산을 O(L)번 반복 => O(L*R)
#     for student in lost: # O(L)
#         # in을 쓰면 매번 순회해서 찾음
#         if student not in reserve: # worst O(R)
#             real_lost.append(student)
#         if reserve and student in reserve: # worst O(R)
#             # in과 remove는 내부적으로 for문 돌리는 것
#             reserve.remove(student) # O(R)
            
#     for student in real_lost: # O(L)
#         # 작은 값을 먼저 확인하므로 정렬이 필요함
#         # 반례: 5, [4, 2], [3, 5]
#         if reserve and student-1 in reserve: # O(R)
#             reserve.remove(student-1) # O(R)
#             answer += 1
#             continue
    
#         if reserve and student+1 in reserve: # O(R)
#             reserve.remove(student+1) # O(R)
#             answer += 1
            
#     return n-len(real_lost)+answer
