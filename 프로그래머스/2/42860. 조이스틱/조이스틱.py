def solution(name):
    answer = 0
    # 상하
    # ord("A") 65 ord("Z") 90
    for s in name:
        answer += min(ord(s)-ord("A"), ord("Z")-ord(s)+1)
    
    # 좌우
    n = len(name)
    move = n - 1
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == "A":
            next_idx += 1
        move = min(move, 2 * i + n - next_idx, i + 2 * (n - next_idx))
        
    answer += move
    return answer