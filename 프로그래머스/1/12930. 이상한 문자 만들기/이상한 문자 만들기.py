def solution(s):
    # 공백은 유지해야 하므로 split대신 split(' ')
    s_list = s.split(' ')
    
    # 공백을 복원해야 하므로(바로 str로 반환할 경우) 단어와 단어 사이의 공백은 공백-1이 됨 => 리스트에 새로 담기
    # 예: "  hello   python   bye   " hello와 python 사이에 공백은 3개지만, 가운데 공백을 기준으로 양쪽 공백만이 담김
    # ['', '', 'hello', '', '', 'python', '', '', 'bye', '', '', '']
    new_list = []
    for i in s_list:
        if i=='':
            new_list.append(i)
        else:
            word = ''
            for idx,value in enumerate(i):
                if idx%2 == 0:
                    word += value.upper()
                else:
                    word += value.lower()
            new_list.append(word)
            
    return ' '.join(new_list)