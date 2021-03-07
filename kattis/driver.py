n = int(input())
cost = [int(x) for x in input().split()]
open = [int(x) for x in input().split()]

total = 0
mincost = cost[0]
time = 0
for gate in range(n-1):
    if cost[gate] < mincost:
        mincost = cost[gate]
    
    total += cost[gate]
    time += 1
    while time < open[gate+1]:
        time += 2
        total += mincost*2

print(total)