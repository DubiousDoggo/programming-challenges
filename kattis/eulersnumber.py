f = 1
e = 1
for i in range(int(input())):
    f *= i+1
    e += 1/f
print(e)