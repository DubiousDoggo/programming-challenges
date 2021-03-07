t = 0
p = ''
for _ in range(int(input())):
    a = input()
    if a == p:
        t += 1
    p = a
print(t)