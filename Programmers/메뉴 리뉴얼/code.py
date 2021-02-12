from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    orders = [sorted(i) for i in orders]

    # 0 으로 초기값을 같은 딕셔너리 선언
    counter = defaultdict(int)
    max_count = defaultdict(int)
    
    for order in orders:
        for c in course:
            if len(order) < c:
                continue
            
            # 단품메뉴의 모든 조합 확인
            combination = combinations(order, c)
            
            for each in combination:
                food = "".join(each)
                
                # 조합 등장횟수 + 1
                counter[food] += 1
                
                # 조합갯수별 최댓값 확인
                if max_count[c] < counter[food]:
                    max_count[c] = counter[food]
                
    answer = []
    for c in course:
        # 조합갯수의 등장횟수가 2보다 작을 경우 pass
        if max_count[c] < 2: continue
        answer += [i[0] for i in counter.items() if len(i[0]) == c and i[1] == max_count[c]]
        
    return sorted(answer)

if __name__ == "__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    result = solution(orders, course)
    print(result)
