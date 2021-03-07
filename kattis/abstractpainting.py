for _ in range(int(input())):
    x, y = (int(x) for x in input().split())
    print(18*pow(6, x+y-2, 10**9+7)*pow(2, (x-1)*(y-1), 10**9+7) % (10**9+7))
