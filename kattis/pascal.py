
def func(n):
    counter = 0
    for i in range(n-1, 1, -1):
      counter += 1
      if n % i == 0:
        break
    return counter

def func2(n):
    if n <= 2:
        return 0
    if n % 2 == 0:
        return n // 2
    for i in range(3, n//2, 2):
        if n % i == 0:
            return n - (n//i)
    return n - 2
                    

for n in range(200):
    print(n, func(n), func2(n))