k, p, n = map(lambda x:int(x), input().split(" "))


# ((k % n) * (p % n)) = (k * p) % n
# k * (p * p * p ...) % n = ((((k % n) * (p % n)) % n) * (p % n)  % n) * (p % n)  % n) * ... )
k_r = k % 1000000007
p_r = p % 1000000007
result = k_r
for i in range(n):
    result = (result * p_r) % 1000000007

print(result)
