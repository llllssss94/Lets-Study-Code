total = 0

for i in range(5):
    s, e = input().split(" ")

    s_hh, s_mm = s.split(":")
    e_hh, e_mm = e.split(":")

    total += (int(e_hh) - int(s_hh) )*60 + int(e_mm) + - int(s_mm)

print(total)