def solution(sizes):
    answer = 0
    
    w_l = 0
    h_l = 0
    
    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]
            
        w_l = max(s[0], w_l)
        h_l = max(s[1], h_l)
    
    answer = w_l * h_l
    
    return answer