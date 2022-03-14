import heapq

def solution(scoville, K):
    answer = 0    
    heapq.heapify(scoville)
    
    # 다 꺼낼때 까지
    while scoville:
        min1 = heapq.heappop(scoville)
        # 방금 전에 섞어서 넣은 음식이 K보다 매운 경우 중지
        if min1 >= K:
            break
        
        # 하나 남은 음식을 꺼낸 경우
        if not scoville:
            if min1 < K:
                answer = -1
            break
        
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + (min2 * 2))
        
        answer += 1
    
    return answer