def solution(dartResult):
    answer = []
    
    
    idx = 0
    for c in dartResult:
        if c == "*":
            if len(answer) < 2:
                answer[-1] = answer[-1] * 2
            else:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            continue
        elif c == "#":
            answer[-1] = answer[-1] * -1
            continue
        if c == "S":
            idx = 0
            continue
        elif c == "D":
            answer[-1] = answer[-1] ** 2
            idx = 0
            continue
        elif c == "T":
            answer[-1] = answer[-1] ** 3
            idx = 0
            continue
        if idx == 0:
            answer.append(int(c))
            idx += 1
        else:
            answer[-1] =  answer[-1] * 10 + int(c)
            idx += 1
            
    return sum(answer)