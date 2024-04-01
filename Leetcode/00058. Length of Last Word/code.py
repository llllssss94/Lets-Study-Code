from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split(" ")[::-1]
        last_word = ""

        for i in range(len(s_list)):
            if s_list[i] != "":
                last_word = s_list[i]
                break

        return len(last_word)