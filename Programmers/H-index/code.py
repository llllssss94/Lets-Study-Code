def solution(citations):
    answer = 0

    max_val = max(citations)

    # 최대값까지만 찾으면 됨
    for i in range(max_val):
        cnt = 0
        # 완전 탐색
        for c in range(len(citations)):
            if citations[c] >= i:
                cnt += 1
        # 위키백과 참조
        if cnt >= i:
            answer = max(answer, min(cnt,i)) 
            
    return answer


citations = [3, 0, 6, 1, 5]
result = solution(citations)

print(result)
