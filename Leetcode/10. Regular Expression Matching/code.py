
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern_idx = 0
        string_idx = 0


        while pattern_idx != len(p):
            if string_idx == len(s):
                break
            pc = p[pattern_idx]
            c = s[string_idx]

            if pattern_idx != len(p) - 1:
                if p[pattern_idx + 1] == '*':
                    pattern_idx += 2
                
                if pc != '.':                    
                    while string_idx < len(s):
                        if s[string_idx] != c:
                            break
                        string_idx += 1
                    if pattern_idx == len(p):
                        break
                    elif p[pattern_idx] == pc:
                        pattern_idx += 1
                else:
                    if pattern_idx == len(p):
                        if c == pc:
                            while string_idx < len(s):
                                string_idx += 1
                            pattern_idx += 1
                        break
                    else:
                        

            # 와일드카드면 무조건 맞다고 보고 
            # 다음문자로가고 다음 패턴으로 가고
            if pc == '.':
                string_idx +=1
                pattern_idx += 1
            elif pc == '*':
                # 직전 문자 가져오기
                last_p = p[pattern_idx - 1]
                if last_p == '.':
                    # 와일드 카드 반복인데 다음 패턴 없으면 끝까지 진행
                    if pattern_idx == len(s) - 1:
                        while string_idx < len(s):
                            string_idx += 1
                    else:
                        # 와일드카드 반복이고 다음 패턴 존재하면 다음패턴 나올때까지 진행
                        while string_idx < len(s):
                            if s[string_idx] == p[pattern_idx + 1]:
                                break
                            string_idx += 1
                    # 반복문자 다음 패턴으로
                    pattern_idx += 1
                else:
                    # 와일드 카드 반복 아니면 이전 문자랑 다른거 나올때까지 진행
                    while string_idx < len(s):
                        if s[string_idx] != last_p:
                            break
                        string_idx += 1
                    # 반복문자 다음 패턴으로
                    # 만약 다음 패턴이 있고 이전 것과 같으면 다음 패턴도 찾았다고 볼 수 있으므로 pattern_idx + 2
                    if pattern_idx != len(p) - 1:
                        if p[pattern_idx+1] == last_p:
                            pattern_idx += 2
                        else:
                            pattern_idx += 1
                    else:
                        pattern_idx += 1
            elif c == pc:
                # 일반 문자인 경우 
                string_idx += 1
                pattern_idx += 1
            else:
                # 다른 문자 발견하면 종료
                if pattern_idx != len(p) - 1:
                    if p[pattern_idx + 1] == '*':
                        pattern_idx += 1
                else:
                    break

        print(string_idx, pattern_idx)
        # 패턴 문자를 모두 발견한 경우엔 pattern_idx == len(p)
        # 패턴 문자를 다 발견했으나 string에 남은 문자열이 있으면 string_idx != len(s)
        if pattern_idx != len(p):
            return False
        
        elif string_idx != len(s):
            return False
        
        return True
                
                
        # 첫번째 패턴과 일치할때 까지 가다가
        # 첫번재 패턴 맞추면 다음 꺼를 확인햇거
        # .면 다음 패턴 문자 만날때까지 쭉 가고
        # + 면 다른 문자 만날때 까지 쭉가고
        # 쭉가고 나서 ., +인 경우엔 패턴 인덱스 2개 증가
        # ., +아니면 인덱스 1개 증가하고 s인덱스도 1개 증가
                
               

            


if __name__ == "__main__":
    s = 'aa'
    p = 'a'

    ret = Solution().isMatch(s, p)
    print(ret)

    
    s = 'aa'
    p = 'a*'

    ret = Solution().isMatch(s, p)
    print(ret)

    
    s = 'aa'
    p = '.*'

    ret = Solution().isMatch(s, p)
    print(ret)

    
    
    s = 'aab'
    p = 'c*a*b'

    ret = Solution().isMatch(s, p)
    print(ret)


    
    s = 'aaa'
    p = 'a*a'

    ret = Solution().isMatch(s, p)
    print(ret)