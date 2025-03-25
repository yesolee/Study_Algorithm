def solution(number, k):

    # 작은 숫자를 앞에서부터 제거!(k번까지만)
    # 스택 활용
    stack = []
    
    for num in number:
        while stack and k>0 and stack[-1]<num:
            stack.pop()
            k -= 1
        stack.append(num)

    if k>0:
        stack = stack[:-k]
    return ''.join(stack)