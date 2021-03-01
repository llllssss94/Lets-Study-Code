def solution(board, moves):
    answer = 0
    
    basket = []
    
    for move in moves:
        for line in board:
            if line[move - 1]:
                if len(basket) > 0 and basket[-1] == line[move - 1]:
                    answer += 2
                    basket.pop(-1)
                else:
                    basket.append(line[move - 1])
                
                line[move - 1] = 0
                break
                    
    return answer

if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]

    result = solution(board, moves)

    print(result)
