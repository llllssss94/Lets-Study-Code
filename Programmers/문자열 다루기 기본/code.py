def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        for c in s:
            try:
                int(c)
            except:
                return False
    else:
        return False
                
    return True