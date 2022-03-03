def solution(x):    
    tx = x
    r = 0
    while x != 0:
        r += x % 10
        x = x // 10
    if tx % r == 0:
        return True
    
    return False