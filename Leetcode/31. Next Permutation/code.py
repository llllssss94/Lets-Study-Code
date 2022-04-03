from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Ordered 데이터
        l = len(nums) - 1
        
        # 뒤에서부터 돌면서 감소하는 문자열의 시작점 찾기
        # 즉, 역순 정렬 된 부분을 찾는 것
        # 왜냐면 역순 정렬 된 부분까지는 끝난 것이고 그럼 그 다음 자릿수를 증가시켜야 하기 때문
        # 감소하는 부분은 끝났기 때문에 감소하는 부분 앞에 자릿수(i-1 번째)를 증가시키고
        # 그 뒤로는 sort 된 얘가 들어가면 됨 -> in place 제약사항있으므로
        # swap으로 처리
        while l > 0:
            if nums[l - 1] < nums[l]:
                break
            l -= 1
        
        
        # 다 역순이면 다음이 없다.
        if l == 0:
            nums[:] = nums[::-1]
        
        else:
            r = len(nums) - 1

            # l - 1 번째 자릿수 다음 숫자를 찾는다.
            while nums[r] <= nums[l-1]:
                r -= 1

            # 찾은 자릿수 바꾸기
            nums[l - 1], nums[r] = nums[r], nums[l - 1]

            # 이제 l부터 끝까지 정렬하면 된다
            # -> 사실 정렬이 되어있음 -> 처음에 역순 정렬 되있는 부분을 찾았기 때문임
            #  뒤집기만 하면 됨
            nums[l:] = nums[l:][::-1]




if __name__ == "__main__":
    nums = [1,2,3]
    ret = Solution().nextPermutation(nums)
    

    nums = [3, 2, 1]
    ret = Solution().nextPermutation(nums)

    
    nums = [1, 1, 5]
    ret = Solution().nextPermutation(nums)