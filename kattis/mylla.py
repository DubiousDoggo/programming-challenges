to_win = int(input())
games = input()

a = 0
h = 0
ar = 0
hr = 0
for w in games:
    if w == "A":
        a += 1
    else:
        h += 1

    if a == 3:
        ar += 1
        a = 0
        h = 0
    if h == 3:
        hr += 1
        a = 0
        h = 0
    
if ar < hr:
    print("Arnar")
else:
    print("Hannes")

