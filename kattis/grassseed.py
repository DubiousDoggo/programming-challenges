c = float(input())
t = 0
for _ in range(int(input())):
    w, h = (float(x) for x in input().split())
    t += w*h*c
print(t)