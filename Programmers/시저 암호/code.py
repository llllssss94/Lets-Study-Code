def solution(s, n):#97 122 65 90
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        elif ord(c) > 96:
            nc = ord(c) + n
            if nc > 122:
                nc = nc - 122 + 96
            answer += chr(nc)
        else:
            nc = ord(c) + n
            if nc > 90:
                nc = nc - 90 + 64
            answer += chr(nc)
        
    return answer