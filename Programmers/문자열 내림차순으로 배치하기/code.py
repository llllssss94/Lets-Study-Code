def solution(s):
    return ''.join(sorted(s, key= lambda x: ord(x), reverse=True))