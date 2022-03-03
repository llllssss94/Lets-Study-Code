def solution(nums):
    answer = 0
    
    u_l = list(set(nums))
    
    answer = min(len(nums)/2, len(u_l))
    
    return answer