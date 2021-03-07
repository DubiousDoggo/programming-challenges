print([x[0]*(x[1]+1)-x[2] for x in [[int(input())]+[[x,sum(int(input()) for _ in range(x))] for x in [int(input())]][0]]][0])
