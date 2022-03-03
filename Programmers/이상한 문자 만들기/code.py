def solution(s):
    answer = ''
    
    i = 0
    for c in s:
        if c == ' ':
            answer += c
            i = 0
        elif i % 2 == 0:
            answer += c.upper()
            i += 1
        else:
            answer += c.lower()
            i += 1
    
    return answer