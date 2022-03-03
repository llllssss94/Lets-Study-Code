def solution(nums):
    answer = 0
    
    from itertools import combinations
    from math import sqrt
    
    for c in combinations(nums, 3):
        num = sum([int(n) for n in c])
        
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer