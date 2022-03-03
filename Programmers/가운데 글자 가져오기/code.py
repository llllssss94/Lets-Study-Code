def solution(s):
    answer = ''
    
    l = len(s)
    if l % 2:
        l = int(l/2)
        answer = s[l]
    else:
        l = int(l/2)
        answer = s[l-1:l+1]
    
    return answer