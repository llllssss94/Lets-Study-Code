from typing import List
from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        answer = 0

        cnt_map = Counter(arr)
        
        i = 0
        # 숫자 3개
        while i < len(arr):
            l = i
            r = len(arr) - 1

            while l < r:
                if arr[l] + arr[r] < target - arr[i]:
                    l += cnt_map[arr[l]]
                elif arr[l] + arr[r] > target - arr[i]:
                    r -= cnt_map[arr[r]]
                else:
                    # Case 분류 다 해주어야 함
                    if arr[i] != arr[l] != arr[r]:  
                        answer += cnt_map[arr[i]] * cnt_map[arr[l]] * cnt_map[arr[r]]
                    elif arr[i] == arr[l] != arr[r]:
                        # nC2
                        answer += cnt_map[arr[i]] * (cnt_map[arr[i]] - 1) * cnt_map[arr[r]] // 2
                    elif arr[i] != arr[l] == arr[r]:
                        # nC2
                        answer += cnt_map[arr[l]] * (cnt_map[arr[l]] - 1) * cnt_map[arr[i]] // 2
                    else:
                        # nC3
                        answer += cnt_map[arr[i]] * (cnt_map[arr[i]] - 1) * (cnt_map[arr[i]] - 2) // 6


                    l += cnt_map[arr[l]]
                    r -= cnt_map[arr[r]]
            
            i += cnt_map[arr[i]]

        return answer % 1000000007


if __name__ == "__main__":
    
    arr = [1,1,2,2,3,3,4,4,5,5]
    target = 8

    ret = Solution().threeSumMulti(arr, target)
    print(ret)


    
    arr = [1,1,2,2,2,2]
    target = 5

    ret = Solution().threeSumMulti(arr, target)
    print(ret)

    
    arr = [0, 0, 0]
    target = 0

    ret = Solution().threeSumMulti(arr, target)
    print(ret)
    
    
    arr = [0, 2, 0]
    target = 2

    ret = Solution().threeSumMulti(arr, target)
    print(ret)