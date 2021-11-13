for _ in range(int(input())):
    print(1+sum(int(x)-1 for x in input().split()[1:]))