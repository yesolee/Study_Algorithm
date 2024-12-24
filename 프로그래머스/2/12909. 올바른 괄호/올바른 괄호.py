def solution(s):
    pair = []
    for i in s:
        try :
            if i == "(":
                pair.append(i)
            else:
                pair.pop()
        except IndexError:
            return False
    return True if len(pair) == 0 else False