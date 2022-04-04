
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        answer = 0

        while True:
            if startValue >= target:
                answer += startValue - target
                break
            
            # 2로 나누어 떨어지면
            if target % 2 == 0:
                # 2로 나누고
                target /= 2
                # 비용 증가
                answer += 1
            else:
                # 목표까지 비용이 증가함
                target += 1
                answer += 1

        return int(answer)

if __name__ == "__main__": 
    startValue = 2
    target = 3

    ret = Solution().brokenCalc(startValue, target)
    print(ret)

    
    startValue = 5
    target = 8

    ret = Solution().brokenCalc(startValue, target)
    print(ret)
    
    startValue = 3
    target = 10

    ret = Solution().brokenCalc(startValue, target)
    print(ret)


    
    startValue = 1
    target = 1000000000

    ret = Solution().brokenCalc(startValue, target)
    print(ret)
    