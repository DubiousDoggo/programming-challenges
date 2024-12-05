n = int(input())
while True:
    text = [input() for _ in range(n)]
    m = max(len(l) for l in text)
    text = [t.ljust(m) for t in text]
    for i in range(m):
        print("".join(text[-1-j][i] for j in range(n)).translate(str.maketrans("|-", "-|")).rstrip())  
    n = int(input())
    if n == 0:
        break
    print("")

