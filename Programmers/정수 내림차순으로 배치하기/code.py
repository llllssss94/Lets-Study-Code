def solution(n):
    return int(''.join(x for x in sorted(str(n), reverse=True)))