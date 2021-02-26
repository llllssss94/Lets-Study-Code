def check(a):
    # 첫자리
    t = a % 10

    # 자릿수 삭제
    a = a // 10

    # 공차
    d = t - (a % 10)

    # 한자릿수 되기 전까지
    while a >= 10:
        # 현재 수 떼기
        t = a % 10

        # 자릿수 삭제
        a = a // 10

        # 공차 확인
        if d != (t - (a % 10)):
            return False
    return True
        
        
    

# 입력
num = int(input())

cnt = 0

for i in range(1, num + 1):
    if check(i):
        cnt += 1

print(cnt)
