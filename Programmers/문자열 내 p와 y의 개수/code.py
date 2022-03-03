def solution(s):
    answer = 0
    
    for c in s.lower():
        if c == 'p':
            answer += 1
        elif c == 'y':
            answer -= 1

    return not(answer)