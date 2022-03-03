def solution(N, stages):
    answer = [0]*(N + 1)
    
    for i in stages:
        answer[i-1] += 1
    
    tmp = 0
    for i in range(len(answer)-1, -1, -1):
        if answer[i] == 0:
            continue
        tmp += answer[i]
        answer[i] = answer[i] / tmp
    
    answer = answer[:-1]
    answer = list(map(lambda x:x[0]+1, sorted(enumerate(answer), key=lambda x:x[1], reverse=True)))
    
    return answer