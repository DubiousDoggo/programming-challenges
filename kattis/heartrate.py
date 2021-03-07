for _ in range(int(input())):
    b, p = (float(x) for x in input().split())
    print(60*(b-1)/p, 60*b/p, 60*(b+1)/p)
