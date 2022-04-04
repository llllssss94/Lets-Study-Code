class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, token in enumerate(sentence.split(' ')):
            if token.startswith(searchWord):
                return i + 1
        
        return -1