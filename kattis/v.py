x, a, b = (int(x) for x in input().split())
c = input()
n = [x for x in '1234567890' if x not in c]
t = 0
m = (a//x+1)*x
while m <= b:
    for i, d in enumerate(reversed(str(m))):
        if d in n:
            m += 
            break
    else:
        t += 1
        m += x
print(t)