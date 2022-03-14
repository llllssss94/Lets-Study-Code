from itertools import combinations
from collections import deque

def solution(clothes):
    answer = 1
    costs = {}
    
    for v, k in clothes:
        if (k,) not in costs:
            costs[(k,)] = 1
        else:
            costs[(k,)] += 1
    
    for v in costs.values():
        answer *= (v + 1)
    
    return answer - 1