from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # s에 존재하는 문자가 한 부분에만 나오도록 분할한다.
        # 최대한 많은 분할이 생길 수 있도록 위 조건이 만족하는 최소 길이로 구분한다.
        answer = []
        parts = []

        chars = {c:False for c in set(s)}
        
        for c in s:
            if chars[c] == True:
                continue
            l, r = 0, len(s) - 1
            
            while l < len(s):
                if s[l] == c:
                    break
                l += 1
            while r > 0:
                if s[r] == c:
                    break
                r -= 1
            
            # 거리 계산을 위해 1부터 시작하도록 입력
            parts.append((l+1, r+1))
            chars[c] = True
        

        ps = 501
        pe = -1
        # 시작점이 빠른 순으로 정렬
        parts.sort(key=lambda x : x[0])
        # 시작점이 끝 지점 안에 있으면 병합
        # 벗어나면 분리
        for start, end in parts:
            if pe < 0:
                pe = end
                ps = start
            elif start <= pe:
                pe = max(pe, end)
                ps = min(ps, start)
            else:
                answer.append(pe - ps + 1)
                ps = start
                pe = end

        # 마지막 부분
        answer.append(pe - ps + 1)
        return answer


if __name__ == "__main__": 
    s = "ababcbacadefegdehijhklij"

    ret = Solution().partitionLabels(s)
    print(ret)


    s = "eccbbbbdec"

    ret = Solution().partitionLabels(s)
    print(ret)