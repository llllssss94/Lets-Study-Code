from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sum_map = []
        for i, r in enumerate(mat):
            r_s = sum(r)
            sum_map.append((r_s, i))

        
        sum_map = sorted(sum_map, key=lambda x : x[0])

        answer = [i for (_, i) in sum_map][:k]
        
        
        return answer


if __name__ == "__main__":
    mat = [
        [1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]
    ]
    k = 3

    ret = Solution().kWeakestRows(mat, k)
    print(ret)

    
    mat = [
        [1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]
    ]
    k = 2

    ret = Solution().kWeakestRows(mat, k)
    print(ret)