word = input()

j = 4
for i in word:
    print("[" + str(int(i) * 10**j) + "]")
    j -= 1

