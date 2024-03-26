from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        v_dict = dict()
        h_dict = dict()
        square_dict = dict()
        for i in range(9):
            for j in range(9):
                num = board[i][j]

                s_idx = str(i//3) + str(j//3) + num

                h_idx = str(i)+num
                v_idx =str(j)+num
                if num != ".":
                    if s_idx not in square_dict:
                        square_dict[s_idx] = 0
                    else:
                        return False
                    if h_idx not in h_dict:
                        h_dict[h_idx] = 0
                    else:
                        return False
                    if v_idx not in v_dict:
                        v_dict[v_idx] = 0
                    else:
                        return False
                        
        return True
    

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board))