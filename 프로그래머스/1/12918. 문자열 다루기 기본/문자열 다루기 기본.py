def solution(s):
    # or는 둘중 하나를 만족하면 True
    if s.isdigit() and len(s) in [4,6]:
        return True
    else:
        return False