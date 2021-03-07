from math import sqrt
n = int(input())
f = 2
c = 1
s = sqrt(n)
while n > 1 and f <= s:
    if n % f:
        f += 1
    else:
        c += 1
        n //= f
        s = sqrt(n)
print(c)
