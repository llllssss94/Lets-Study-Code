from typing import List
from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        cnt_map = defaultdict(list)

        for n, v in cnt.items():
            cnt_map[v].append(n)

        max_keys = list(cnt_map.keys())
        max_keys.sort(reverse=True)

        answer = []
        for n in max_keys:
            next_val = cnt_map[n]
            if len(answer) + len(next_val) > k:
                break
            else:
                answer += next_val

        return answer


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    ret = Solution().topKFrequent(nums, k)
    print(ret)


    
    nums = [1,1,1,2,2,3]
    k = 2

    ret = Solution().topKFrequent(nums, k)
    print(ret)


    
    nums = [3,0,1,0]
    k = 1

    ret = Solution().topKFrequent(nums, k)
    print(ret)

    
    
    nums = [1, 2]
    k = 2

    ret = Solution().topKFrequent(nums, k)
    print(ret)