def solution(s):
    # or는 둘중 하나를 만족하면 True
    # and는 둘 다 만족해야만 True
    return s.isdigit() and len(s) in [4,6]