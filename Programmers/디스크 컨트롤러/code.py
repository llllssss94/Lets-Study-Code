import heapq

def solution(jobs):
    answer = 0
    
    last = -1
    cur = 0
    i = 0
    # 모든 job을 실행할 때 까지
    job_time = []
    while i < len(jobs):        
        # 현재 시간에 실행 가능한 job들을 대기 시간 짧은 순으로 정렬해서 추가
        for job in jobs:
            if  last < job[0] <= cur:
                heapq.heappush(job_time, (job[1], job[0]))
        # 실행가능한 job이 없으면 시간 진행
        if not job_time:
            cur += 1
            continue
        
        # 실행가능한 job들 중 가장 실행시간이 짧은 job 실행
        cur_job = heapq.heappop(job_time)
        
        last = cur
        # 실행한 job 만큼 시간 진행
        cur += cur_job[0]
        # 방금 실행한 job의 최종 대기시간 기록
        answer += cur - cur_job[1]
        i += 1
        
    return answer // i