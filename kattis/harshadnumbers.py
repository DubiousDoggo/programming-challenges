def isHarshad(n: int):
    return n % sum(int(x) for x in str(n)) == 0

n = int(input())
while not isHarshad(n):
    n += 1
print(n)