import itertools
n, t = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
if t == 1:
    for x, y in itertools.combinations(a, 2):
        if x != y and x + y == 7777:
            print("Yes")
            break
    else:
        print("No")
elif t == 2:
    u = set()
    for i in a:
        if i in u:
            print("Contains duplicate")
            break
        u.add(i)
    else:
        print("Unique")
elif t == 3:
    counts = {}
    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
        if counts[i] > n / 2:
            print(i)
            break
    else:
        print(-1)
elif t == 4:
    s = sorted(a)
    if n & 1:
        print(s[n//2])
    else:
        print(s[n//2-1],s[n//2])
elif t == 5:
    print(*(x for x in sorted(a) if 100 <= x < 1000))