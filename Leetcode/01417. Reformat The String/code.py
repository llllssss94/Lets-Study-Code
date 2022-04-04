class Solution:
    def reformat(self, s: str) -> str:
        answer = ''
        # 알파벳, 숫자 분리
        alpa = list(filter(lambda x : not x.isdigit(), s))
        digits = list(filter(lambda x : x.isdigit(), s))
        
        # 만약 pair가 안생기면 못 만듬
        if abs(len(alpa) - len(digits)) > 1:
            return answer
        else: 
            for i in range(max(len(alpa), len(digits))):
                
                if len(alpa) > len(digits):
                    if alpa:
                        answer += alpa.pop()
                    if digits:
                        answer += digits.pop()
                else:
                    if digits:
                        answer += digits.pop()
                    if alpa:
                        answer += alpa.pop()

        return answer