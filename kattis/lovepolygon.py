def arrowcount():
    n = int(input())
    loves = {a: b for _ in range(n) for a, b in [input().split()]}
    if n & 1:
        return -1
    lovecount = {k: 0 for k in loves.keys()}
    unloved = {k for k in loves.keys()}
    for v in loves.values():
        lovecount[v] += 1
        unloved.discard(v)
    loves = {k: v for k, v in loves.items() if v == k or loves[v] != k}
    cuts = 0
    while len(loves):
        if not len(unloved):
            unloved.add(next(iter(loves)))
        while len(unloved):
            u = unloved.pop()
            v = loves[u]
            loves.pop(u)
            if v in loves.keys():
                w = loves[v]
                if w in loves.keys():
                    lovecount[w] -= 1
                    if lovecount[w] == 0:
                        unloved.add(w)
                loves.pop(v)
            cuts += 1
    return cuts


print(arrowcount())