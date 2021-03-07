t = 0
for r in input().split(';'):
    t += 1
    if '-' in r:
        a, b = (int(x) for x in r.split('-'))
        t += b - a
print(t)