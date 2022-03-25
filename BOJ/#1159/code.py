answer = []

c_dict = {}

n = int(input())

for _ in range(n):
    name = input()[0]
    if name not in c_dict:
        c_dict[name] = 1
    else:
        c_dict[name] += 1

for k, v in c_dict.items():
    if v >= 5:
        answer.append(k[0])

if len(answer) < 1:
    answer = "PREDAJA"
else:
    answer = ''.join(sorted(answer))

print(answer)