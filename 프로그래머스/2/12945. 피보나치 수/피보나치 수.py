def solution(n):
    # n이 1000보다 큼 => 재귀X
    a, b = 0,1 
    for _ in range(2, n+1):
        a, b = b, a+b
    return b%1234567