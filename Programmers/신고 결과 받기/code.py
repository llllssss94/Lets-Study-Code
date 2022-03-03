def solution(id_list, report, k):
    answer = []
    
    emailed = dict.fromkeys(id_list)
    reported = dict.fromkeys(id_list)
    
    for key in id_list:
        emailed[key] = 0
        reported[key] = []
    
    for r in report:
        _from, _to = r.split(" ")
        reported[_to].append(_from)
        
    for _report in reported.values():
        cnt = set(_report)
        if len(cnt) >= k:
            for reporter in cnt:
                emailed[reporter] += 1
    
    answer = list(emailed.values())
    
    return answer