def solution(d, budget):
    answer = 0
    d.sort()
    
    s = 0
    for i in range(0, len(d)):
        if s + d[i] <= budget:
            s += d[i]
            answer += 1
        else:
            break
        
    return answer