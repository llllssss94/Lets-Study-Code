from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Backtracking 

        # 긴거 부터 탐색하도록 정렬
        arr.sort(key=lambda l: len(l), reverse=True)
        
        # 재귀 dfs
        answer = self.recurse('', arr, 0)

        return len(answer)
    
    # dfs
    def recurse(self, cur, arr, i):
        if i == len(arr):
            return cur
        
        # 더할 수 잇는지 보고 못 더하면 탐색 안함
        is_valid = True
        if len(set(cur+arr[i])) < len(cur+arr[i]):
            is_valid = False
        
        l = ''
        if is_valid:
            l = self.recurse(cur + arr[i], arr, i+1)
        
        r = self.recurse(cur, arr, i+1)

        if len(l) > len(r):
            return l
        else:
            return r
            
        

if __name__ == "__main__":
    arr = ["un","iq","ue"]

    ret = Solution().maxLength(arr)
    print(ret)

    
    arr = ["cha","r","act","ers"]

    ret = Solution().maxLength(arr)
    print(ret)

    
    
    arr = ["aa","bb"]

    ret = Solution().maxLength(arr)
    print(ret)