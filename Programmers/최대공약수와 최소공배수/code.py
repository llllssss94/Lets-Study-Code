def solution(n, m):
    tn = n
    tm = m
    
    while m != 0:
        r = n % m
        n = m
        m = r
        
    return [n, (tn*tm)/n]