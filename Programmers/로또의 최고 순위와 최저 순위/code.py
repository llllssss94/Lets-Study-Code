def solution(lottos, win_nums):
    answer = []    
    
    unmatched = set(win_nums) - set(lottos)
    min_win = len(win_nums) - len(unmatched)
    
    wild_card = 0
    for num in lottos:
        if num == 0:
            wild_card += 1
    
    for cnt in [min_win + wild_card, min_win]:
        if cnt < 2:
            answer.append(6)
        else:
            answer.append(7 - cnt)
    
    return answer