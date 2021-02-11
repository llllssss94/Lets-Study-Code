def solution(w,h):

    # 더 긴 방향 찾기
    q = max(w, h)
    r = min(w, h)

    # 최대공약수 찾기 - 유클리드 호제법
    while r != 0:
        t = q % r
        q = r
        r = t

    # 전체 갯수에서 잘리는 사각형 수 빼기 - 귀납적으로 찾기
    return (w * h) - (w + h - q)

if __name__ == "__main__":
    w, h = input().split(' ')
    result = solution(int(w), int(h))
    print(result)
