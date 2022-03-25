class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0

        last = ''
        while i < len(name) and j < len(typed):
            # 같은 문자면 1칸 씩 이동, 이전 typed 문자 저장
            if name[i] == typed[j]:
                last = typed[j]
                i += 1
                j += 1
            else:
                # 다른 경우
                # 만약 이전 문자와 현재 typed 문자가 다르면 실패
                if typed[j] != last:
                    return False
                else:
                    j += 1
        
        if i < len(name):
            return False

        if j < len(typed):
            while last == typed[j]:
                last = typed[j]
                j += 1
                if j == len(typed):
                    break
            if j != len(typed):
                return False
        
        return True

if __name__ == "__main__":
    name = "alex"
    typed = "aaleex"

    ret = Solution().isLongPressedName(name, typed)
    print(ret)



    name = "saeed"
    typed = "ssaaedd"

    ret = Solution().isLongPressedName(name, typed)
    print(ret)


    name = "leelee"
    typed = "lleeelee"

    ret = Solution().isLongPressedName(name, typed)
    print(ret)


    name = "a"
    typed = "b"

    ret = Solution().isLongPressedName(name, typed)
    print(ret)


    name = "alex"
    typed = "aaleexa"

    ret = Solution().isLongPressedName(name, typed)
    print(ret)


    name = "vtkgn"
    typed = "vttkgnn"

    ret = Solution().isLongPressedName(name, typed)
    print(ret)

    
    name = "zlexya"
    typed = "aazlllllllllllllleexxxxxxxxxxxxxxxya"

    ret = Solution().isLongPressedName(name, typed)
    print(ret)
