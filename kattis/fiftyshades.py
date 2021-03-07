t = 0
for _ in range(int(input())):
    i = input().lower()
    if 'rose' in i or 'pink' in i:
        t += 1
if t > 0:
    print(t)
else:
    print('I must watch Star Wars with my daughter')