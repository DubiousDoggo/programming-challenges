import sys
d = {}
for line in sys.stdin:
    c, *a = line.split()
    if c == 'define':
        v, n = a
        d[n] = int(v)
    else:
        x, c, y = a
        try:
            x, y = d[x], d[y]
        except:
            print('undefined')
        else:
            if c == '=':
                print(str(x == y).lower())
            if c == '<':
                print(str(x < y).lower())
            if c == '>':
                print(str(x > y).lower())
