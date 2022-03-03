def solution(s):
    answer = 1
    
    if s[0] == '-':
        answer = -1
        s = s[1:]
    
    return answer * int(s)