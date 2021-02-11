# 월, 일 입력
m, d = input().split(' ')
m = int(m)
d = int(d)

# 나머지를 인덱스로 0 ~ 6
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date_sum = 0

# 월 합산
for i in range(m - 1):
    date_sum += dates[i]

# 일 합산
date_sum += d

# 7단위로 나누기
idx = date_sum % 7

print(days[idx])

