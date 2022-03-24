from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weights = sorted(people)
        answer = 0

        l = 0
        r = len(people) - 1

        while l <= r:
            # 최대 두명까지 태움
            l_num = weights[l]
            r_num = weights[r]

            # 두명 태울 수 있으면
            if l_num + r_num <= limit:
                l += 1
                r -= 1
                answer += 1
            else:
                # 못 태우면 무거운 친구부터
                r -= 1
                answer += 1
        

        return answer




if __name__ == "__main__": 
    people = [1,2]
    limit = 3

    ret = Solution().numRescueBoats(people, limit)
    print(ret)

    
    people = [3, 2, 2, 1]
    limit = 3

    ret = Solution().numRescueBoats(people, limit)
    print(ret)

    
    people = [3, 5, 3, 4]
    limit = 5

    ret = Solution().numRescueBoats(people, limit)
    print(ret)

    
    people = [5,1,4,2]
    limit = 6

    ret = Solution().numRescueBoats(people, limit)
    print(ret)