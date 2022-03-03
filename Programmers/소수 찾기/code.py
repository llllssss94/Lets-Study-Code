import math

def solution(n):
    answer = [True] * (n + 1)
    p = int(math.sqrt(n)) + 1
    
    answer[0] = False
    answer[1] = False
    
    for i in range(2, p):
        if answer[i] == True:
            for j in range(2*i, n+1, i):
                answer[j] = False
    
    return answer.count(True)