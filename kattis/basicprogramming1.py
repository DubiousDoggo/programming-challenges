n, t = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
if t == 1:
    print(7)
elif t == 2:
    if a[0] > a[1]:
        print("Bigger")
    elif a[0] == a[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    if a[0] >= a[1] >= a[2] or a[0] <= a[1] <= a[2]:
        print(a[1])
    elif a[1] >= a[0] >= a[2] or a[1] <= a[0] <= a[2]:
        print(a[0])
    elif a[1] >= a[2] >= a[0] or a[1] <= a[2] <= a[0]:
        print(a[2])
elif t == 4:
    print(sum(a))
elif t == 5:
    print(sum(x for x in a if x % 2 == 0))
elif t == 6:
    print(''.join(chr(x % 26 + 97) for x in a))
elif t == 7:
    cycle = [False] * len(a)
    i = 0
    while True:
        i = a[i]
        if i >= len(a):
            print("Out")
            break
        if i == len(a) - 1:
            print("Done")
            break
        if cycle[i]:
            print("Cyclic")
            break
        cycle[i] = True
