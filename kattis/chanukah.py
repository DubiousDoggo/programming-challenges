for i in range(int(input())):
    k, n = (int(x) for x in input().split())
    print(k, n*(n+1)//2 + n)
