import re


def isSheldon(n):
    b = bin(n)[2:]
    

#x, y = (int(x) for x in input().split())
#print(sum(isSheldon(i) for i in range(x, y+1)))


for p in range(63):
    t = 0
    for i in range(2**p, 2**(p+1)):
        if isSheldon(i):
            print(i, bin(i))
            t += 1
    print(2**p, '-', 2**(p+1), ':', t)
