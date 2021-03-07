i = 501
d = i / 2
while True:
    print(int(i))
    r = input()
    if r == 'higher':
        i += d
    if r == 'lower':
        i -= d
    if r == 'correct':
        break
    d /= 2