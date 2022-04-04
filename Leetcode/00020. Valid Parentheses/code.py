
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in [")", "]", "}"]:
                    last = stack.pop()
                    if last != pairs[c]:
                        return False
                else:
                    stack.append(c)
        if stack:
            return False
        
        return True


if __name__ == "__main__":
    s = "()"

    ret = Solution().isValid(s)
    print(ret)

    
    s = "()[]{}"

    ret = Solution().isValid(s)
    print(ret)

    
    s = "(]"

    ret = Solution().isValid(s)
    print(ret)