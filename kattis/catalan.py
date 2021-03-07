
def catalan(n):
    num = 1
    den = 1
    for k in range(2, n+1):
        num *= n+k
        den *= k
    return num // den


for _ in range(int(input())):
    print(catalan(int(input())))
