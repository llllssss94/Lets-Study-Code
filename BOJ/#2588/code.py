n = input()
m = input()

rm = m[::-1]
n = int(n)

for i in rm:
    print(n * int(i))

print(n * int(m))
