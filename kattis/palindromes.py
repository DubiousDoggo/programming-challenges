
def countMaxSymm(string: str, start: int, end: int):
    length = len(string)
    counts = ([0]*(length), [1]*length)
    for n in range(start, end-1):
        i = n
        j = n + 1
        while i >= start and j < end:
            if string[i] != string[j]:
                break
            counts[0][n] += 1
            i -= 1
            j += 1
    for n in range(start, end):
        i = n - 1
        j = n + 1
        while i >= start and j < end:
            if string[i] != string[j]:
                break
            counts[1][n] += 1
            i -= 1
            j += 1
    return counts


def countSymm(maxcounts, start: int, end: int):
    even, odd = maxcounts
    count = 0
    mid = start + (end-start)//2
    for i in range(start, mid):
        if odd[i] < i-start+1:
            count += odd[i]
        else:
            count += i-start+1
        if even[i] < i-start+1:
            count += even[i]
        else:
            count += i-start+1
    for i in range(mid, end):
        if odd[i] < end-i:
            count += odd[i]
        else:
            count += end-i
        if even[i] < end-i-1:
            count += even[i]
        else:
            count += end-i-1
    return count


def test(n, m):
    import random
    name = ''.join(random.choice('abcdefgh') for _ in range(n))
    mins = len(name)
    maxe = 0
    cases = []
    for _ in range(m):
        s = random.randint(0, n-1)
        e = random.randint(s+1, n)
        if s < mins:
            mins = s
        if e > maxe:
            maxe = e
        cases.append((s, e))
    maxcounts = countMaxSymm(name, mins, maxe)
    for s, e in cases:
        print(countSymm(maxcounts, s, e))

def main():
    name = input()
    mins = len(name)
    maxe = 0
    cases = []
    for _ in range(int(input())):
        s, e = (int(x) for x in input().split())
        s -= 1
        if s < mins:
            mins = s
        if e > maxe:
            maxe = e
        cases.append((s, e))
    maxcounts = countMaxSymm(name, mins, maxe)
    for s, e in cases:
        print(countSymm(maxcounts, s, e))

if __name__ == "__main__":
    test(100000, 10000)