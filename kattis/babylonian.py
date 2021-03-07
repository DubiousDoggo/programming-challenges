for _ in range(int(input())):
    i = [int(x or 0) for x in input().split(',')]
    print(sum(n*60**p for p, n in enumerate(reversed(i))))