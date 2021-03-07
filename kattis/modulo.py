s = set()
t = 0
for _ in range(10):
    i = int(input()) % 42
    if i not in s:
        s.add(i)
        t += 1
print(t)
