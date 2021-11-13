import math
pattern = [int(i) for _ in range(3) for i in input().split()]
order = [pattern.index(i) for i in range(1,10)]
total = 0
for i in range(len(order)-1):
    a, b = order[i], order[i+1]
    total += math.hypot(a//3 - b//3, a%3 - b%3)
print(total)