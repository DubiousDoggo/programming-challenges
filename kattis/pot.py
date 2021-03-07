t = 0
for _ in range(int(input())):
    i = input()
    t += int(i[:-1])**int(i[-1])
print(t)