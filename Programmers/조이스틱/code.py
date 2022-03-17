def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = 10e9
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_case = name[-i:] + name[:-i]
        right_case = name[i:] + name[:i]
        for n in [left_case, right_case[0]+right_case[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            cur_cost = i + len(n)-1
            for c in map(ord, n):
                cur_cost += min(c - ord('A'), ord('Z') - c + 1)

            answer = min(answer, cur_cost)

    return answer