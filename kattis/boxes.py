n = int(input())
parent = [int(x)-1 for x in input().split()]
childcount = [0] * n
for i in range(n):
    while i != -1:
        childcount[i] += 1
        i = parent[i]

q = int(input())
for _ in range(q):
    l = {int(x)-1 for x in input().split()[1:]}
    count = 0
    for b in l:
        i = parent[b]
        while i != -1:
            if i in l:
                break
            i = parent[i]
        else:
            count += childcount[b]
    print(count)



