
def chromatic(g):
    # edgeless graph
    if len(g) == 1:
        return 1

    # trim off single node chains
    # trivially two-colorable
    q = set(g.keys())
    while len(q):
        e = q.pop()
        if len(g[e]) == 1:
            for b in g[e]:
                g[b].remove(e)
                q.add(b)
            g.pop(e)

    # tree graph
    if len(g) <= 2:
        return 2

    minvert = len(g)
    maxvert = 0
    for _, v in g.items():
        if len(v) > maxvert:
            maxvert = len(v)
        if len(v) < minvert:
            minvert = len(v)

    # cycle graph
    if maxvert == 2:
        return 2 + len(g) % 2

    # complete graph
    if minvert == len(g)-1:
        return len(g)

    for k in range(3, maxvert):
        raise RuntimeError()  # TODO brue force

    return maxvert


g = {i: {int(x) for x in input().split()} for i in range(int(input()))}
print(chromatic(g))
