def solution(numbers, hand):
    answer = ''
    left = [0, 0]
    right = [0, 2]
    keypad = {1: [3, 0], 2: [3, 1], 3: [3, 2],\
              4: [2, 0], 5: [2, 1], 6: [2, 2],\
              7: [1, 0], 8: [1, 1], 9: [1, 2],\
              0: [0, 1]}
    
    
    for i in numbers:
        p = keypad[i]
        l_d = abs(left[0] - p[0]) + abs(left[1] - p[1])
        r_d = abs(right[0] - p[0]) + abs(right[1] - p[1])
        
        if p[1] == 2:
            answer += 'R'
            right = p
        elif p[1] == 0:
            answer += 'L'
            left = p
        else:
            if l_d == r_d:
                if hand == "right":
                    answer += 'R'
                    right = p
                else:
                    answer += 'L'
                    left = p
            elif l_d < r_d:
                answer += 'L'
                left = p
            else:
                answer += 'R'
                right = p
                
    return answer