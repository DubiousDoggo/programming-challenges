n = int(input())
t = 0
for _ in range(n):
    a, b = (float(x) for x in input().split())
    t += a * b
print(t)